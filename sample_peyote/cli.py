from typing import Optional
import argh

from sample_peyote.core import SampleGenerator

@argh.arg('-t', '--topic', help='Topic for your dataset ideas')
@argh.arg('-n', type=int, help='Number of dataset ideas to choose from')
@argh.arg('-s', '--silent', help='Suppress print output')
@argh.arg('-p', '--path', help='Path in wich to create a new directory to save your samples and associated metadata')
def run(
    topic=None,
    n=5,
    silent=False,
    path=".",
):
    if not silent:
        print("")
        print(80*"=")
        print("\tWelcome to Sample Peyote!")
        print("\tLet's hallucinate some data!\n")
        print("\tWarning: RUNNING SAMPLE PEYOTE COSTS MONEY.\n\tEach run of Sample Peyote costs about $0.05 worth of OpenAI credits.")
        print(80*"=")
        print("")

    sammy = SampleGenerator(print_output=(not silent))

    if topic == None:
        topic = input('Please pick a topic (e.g. data science, fruit, zombies).\n  You can also hit Enter to choose no topic.\n: ') or None

    sammy.generate_dataset_idea_list(
        topic=topic,
        n=n,
    )

    if n>1:
        dataset_index = int(input("\nChoose the number corresponding to the dataset you'd like to generate.\n You can also hit Enter to choose the first topic by default.\n: ") or "1")
    else:
        dataset_index = 1

    sammy.select_dataset_by_index(index=dataset_index-1)

    path = f"{path}/{sammy.run_id}-{sammy.dataset_idea.slug}"
    sammy.save(path=path)

    if not silent:
        print("")
        print("Done!")

parser = argh.ArghParser()
parser.add_commands([run])
parser.set_default_command(run)

def main():
    parser.dispatch()

if __name__ == '__main__':
    main()