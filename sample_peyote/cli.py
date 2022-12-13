import argh

from sample_peyote.core import SampleGenerator

def run():
    print("")
    print(80*"=")
    print("\tWelcome to Sample Peyote!")
    print("\tLet's hallucinate some data!")
    print(80*"=")
    print("")

    sammy = SampleGenerator(print_output=True)

    topic = input('Please pick a topic (e.g. data science, fruit, zombies).\n  You can also hit Enter to choose no topic.\n: ') or None
    sammy.generate_dataset_idea_list(topic=topic)

    dataset_index = int(input("\nChoose the number corresponding to the dataset you'd like to generate.\n You can also hit Enter to choose the first topic by default.\n: ") or "1")
    sammy.select_dataset_by_index(index=dataset_index-1)

    path = f"data/{sammy.run_id}-{sammy.dataset_idea.slug}"
    sammy.save(path=path)

    print("")
    print("Done!")

parser = argh.ArghParser()
parser.add_commands([run])
parser.set_default_command(run)

def main():
    parser.dispatch()

if __name__ == '__main__':
    main()