import datetime
import json
import os
import random
import re
from typing import List, Optional
from io import StringIO

import openai
import pandas as pd
# from pydantic import BaseModel

from sample_peyote.types import DatasetIdea, Table, Sample
from sample_peyote.util import indent

class SampleGenerator(object):

    run_id : str
    print_output : str

    topic : str

    dataset_idea_prompt : str
    dataset_idea_response_text : str
    dataset_idea_list : List[DatasetIdea]

    dataset_index : int
    dataset_idea : DatasetIdea

    table_list_prompt : str
    table_list_response_text : str
    table_list : List[Table]

    sample_prompt_list : List[str]
    sample_response_text_list : List[str]
    sample_list : List[Sample]

    def __init__(
        self,
        run_id:Optional[str]=None,
        print_output:bool=False,
    ):
        if run_id == None:
            now = datetime.datetime.now()
            run_id = datetime.datetime.strftime(now, "%y%m%d-%H%M%S")

        self.run_id = run_id
        self.print_output = print_output

    def generate_dataset_idea_list(
        self,
        topic:Optional[str]=None,
        n:int=5,
    ) -> List[DatasetIdea]:

        if self.print_output:
            if topic == None:
                log_str = "Generating ideas for datasets..."
            else:
                log_str = f"Generating ideas for datasets related to {topic}..."

            print("")
            print(log_str)

        self.topic = topic

        if topic != None:
            topic_prompt = f" Each dataset should be at least somewhat related to {topic}."
        else:
            topic_prompt = ""

        self.dataset_idea_prompt = f"""Please create a list of {n} ideas for types of synthetic tabular data, with descriptions for the data they would contain, and what they might be useful for.{topic_prompt}

    Each item in the list should follow this format:
    * [Name of the dataset] Data: This dataset would contain [description for the data it contains]. It could be used to [what it might be useful for].
    """

        self.dataset_idea_response_text = self._get_openai_response_text(
            model="text-davinci-003",
            prompt=self.dataset_idea_prompt,
            temperature=0.6,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=1
        )

        groups_list = re.findall(
            "\d+\. (.* Data): This dataset would contain (.*). It could be used to (.*)\.",
            self.dataset_idea_response_text
        )
        group_names = ["name", "about", "use_cases"]
        dataset_idea_list = [DatasetIdea(**dict(zip(group_names, groups))) for groups in groups_list]

        if self.print_output:
            print("")
            print("Here are five ideas for datasets:")
            print(indent(self.dataset_idea_response_text, 4))

        self.dataset_idea_list = dataset_idea_list
        return self.dataset_idea_list

    def select_dataset_by_index(
        self,
        index:int,
    ):
        self.dataset_index = index
        self.dataset_idea = self.dataset_idea_list[index]

        self.table_list = self._generate_table_list_from_dataset_idea(self.dataset_idea)

        if self.print_output:
            print("")
            print("Generating sample data for each of these tables...")

        self.sample_prompt_list = []
        self.sample_response_text_list = []
        self.sample_list = []
        for table in self.table_list:
            self._generate_sample_from_table(table)


    def _generate_table_list_from_dataset_idea(
        self,
        dataset_idea:DatasetIdea,
        n:Optional[int]=None,
    ) -> List[Table]:

        if self.print_output:
            print("")
            print(f"Generating table descriptions for {dataset_idea.name}...")
        
        if n == None:
            n = random.randint(4,8)

        self.table_list_prompt = f"""Please create a list of {n} tables that would be important parts of a database for {dataset_idea.name} data. This dataset would contain {dataset_idea.about}. It could be used to {dataset_idea.use_cases}.
        
    For each table, please
    1. describe what a row in the table would be.
    2. list the columns
    3. note which columns should be foreign keys to specific other tables
    4. include a column or columns for timestamps, if appropriate

    Most tables should have between 6 and 20 columns.

    Each item in the list should follow this format:
    * [Name of the table]: This table contains [Description of what a row is]. Columns: [List of columns, separated by commas]"
    """

        self.table_list_response_text = self._get_openai_response_text(
            model="text-davinci-003",
            prompt=self.table_list_prompt,
            temperature=0.6,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=1
        )

        groups_list = re.findall(
            "\d+\. (.*): (This table contains .*)\. Columns: (.*)",
            self.table_list_response_text,
        )
        group_names = ["name", "description", "columns"]
        self.table_list = [Table(**dict(zip(group_names, groups))) for groups in groups_list]

        if self.print_output:
            print("")
            print(f"Here are table descriptions for {dataset_idea.name}:")
            print(indent(self.table_list_response_text, 4))

        return self.table_list

    def _generate_sample_from_table(
        self,
        table:Table,
    ):
        if self.print_output:
            print("")
            print(f"Generating sample data for {table.name}...")

        prompt = f"""Please generate a table of synthetic {table.name} data containing {table.description}.

    It should have 20 rows, and the following columns: {table.columns}.
    Please use a good variety of values in each field.
    It should be formatted as a csv.
    """
        self.sample_prompt_list.append(prompt)

        response_text = self._get_openai_response_text(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        self.sample_response_text_list.append(response_text)

        new_sample = Sample(
            table_name=table.name,
            csv=response_text,
        )
        self.sample_list.append(new_sample)

        if self.print_output:
            print(response_text)

        return new_sample

    def save(
        self,
        path:str,
    ):
        #!!! This will fail if called before everything is successfully instantiated.

        if self.print_output:
            print("")
            print(f"Saving all assets to {path}...")

        os.mkdir(path)

        #Save dataset_ideas to a single file
        with open(f"{path}/dataset_ideas.json", "w") as file_:
            file_.write(json.dumps({
                "run_id" : self.run_id,
                "prompt" : self.dataset_idea_prompt,
                "response_text": self.dataset_idea_response_text,
                "topic" : self.topic,
                "dataset_ideas" : [json.loads(dataset.json()) for dataset in self.dataset_idea_list],
            }, indent=2))

        #Save table JSON to a single file
        with open(f"{path}/tables-{self.dataset_idea.slug}.jl", "w") as file_:
            file_.write("\n".join([table.json() for table in self.table_list]))

        #Save each sample to its own
        for i, sample in enumerate(self.sample_list):
            table = self.table_list[i]
            with open(f"{path}/{table.slug}.csv", "w") as file_:
                file_.write(sample.csv)

        #Save markdown summary
        with open(f"{path}/summary-{self.dataset_idea.slug}.md", "w") as file_:
            file_.write(self.render_markdown())
    
    def render_markdown(self):
        table_str = ""
        for table in self.table_list:
            table_str += f"* {table.name}: {table.description}\n"

        sample_str = ""
        for sample in self.sample_list:
            try:
                sample_md_table = pd.read_csv(StringIO(sample.csv)).to_markdown()
            except pd.errors.ParserError:
                sample_md_table = sample.csv+"\n`CSV parsing error`"
            sample_str += f"#### {sample.table_name}\n{sample_md_table}\n"
        
        sample_prompt_str = ""
        for i in range(len(self.sample_prompt_list)):
            sample_prompt_str += f"""
```
{self.sample_prompt_list[i]}
```

{self.sample_response_text_list[i]}
"""

        return f"""
# {self.dataset_idea.name}

This dataset contains {self.dataset_idea.about}. It could be used to {self.dataset_idea.use_cases}.

run_id: `{self.run_id}`

topic: `{self.topic}`

### Tables
{table_str}

### Samples
{sample_str}

### Prompts and responses
```
{self.dataset_idea_prompt}
```

{self.dataset_idea_response_text}

```
{self.table_list_prompt}
```

{self.table_list_response_text}
"""

    def _get_openai_response_text(
        self,
        model:str,
        prompt:str,
        temperature:float,
        max_tokens:int,
        top_p:float,
        frequency_penalty:float,
        presence_penalty:float,
    ) -> str:

        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )

        response_text = response.choices[0].text
        return response_text

