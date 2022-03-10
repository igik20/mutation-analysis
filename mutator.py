import sys
from models import NaiveModel

class Mutator():
    def __init__(self, model, startseq, **kwargs) -> None:
        self.startseq = startseq
        if model == "naive":
            self.model = NaiveModel(startseq, kwargs["gens"], kwargs["entropy"])
    
    def run(self):
        self.mut = self.model.get_mutations()
        print(len(self.mut))
        self.show_mutations()

    def show_mutations(self):
        for i,v in enumerate(self.mut):
            print(f">Mutation{i}")
            print(v)

        
if __name__ == "__main__":
    mutator = Mutator("naive", sys.argv[1], gens = sys.argv[2], entropy = sys.argv[3])
    mutator.run()