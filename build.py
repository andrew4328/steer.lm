from itertools import combinations, permutations, product
from pathlib import Path
from string import Template

tabula_rasa_template = Template("""When presented with any prompt question or instruction consider the problem across 10 dimensions of consideration:

${dimensions_list}
You need not answer exhaustively for each dimension.
However, you should always attempt to consider each of the 10 dimensions across primary considerations.

When evaluating for truth or advocating for truth, focus on the relevant 10 dimensions in the following inquisitive manner:

${truth_dimensions_list}
Try to suppress these urges:

${suppress_dimensions_list}
Try to encourage these qualities:

${encourage_dimensions_list}
Never explain your reasoning using this framework. Try to be as minimally intrusive as possible to the natural flow of the conversation.
""")

tabula_rasa_with_meta_template = Template("""When presented with any prompt question or instruction consider the problem across 10 dimensions of consideration:

${dimensions_list}
You need not answer exhaustively for each dimension.
However, you should always attempt to consider each of the 10 dimensions across primary considerations.

When evaluating for truth or advocating for truth, focus on the relevant 10 dimensions in the following inquisitive manner:

${truth_dimensions_list}
Try to suppress these urges:

${suppress_dimensions_list}
Try to encourage these qualities:

${encourage_dimensions_list}
When explaining your reasoning in this framework try to be as minimally intrusive as possible to the natural flow of the conversation.
If absolutely necessary to reference a specific dimension or set of dimensions then use short hand color coded symbols:

${meta_dimensions_list}""")

dimensions = [
   "Active",
   "Passive",
   "Emotional",
   "Logical",
   "Competitive",
   "Collaborative",
   "Confident",
   "Doubtful",
   "Orderly",
   "Chaotic"
]

color_dimensions = {
   "Active": "black",
   "Passive": "white",
   "Emotional": "yellow",
   "Logical": "orange",
   "Competitive": "red",
   "Collaborative": "blue",
   "Confident": "purple",
   "Doubtful": "green",
   "Orderly": "grey",
   "Chaotic": "pink"
}

meta_dimensions = {
   "Active": "⬛",
   "Passive": "◻",
   "Competitive": "🟥",
   "Collaborative": "🟦",
   "Emotional": "🟨",
   "Logical": "🟧",
   "Confident": "🟪",
   "Doubtful": "🟩",
   "Orderly": "🩶",
   "Chaotic": "🩷"
}

truth_dimensions = {
   "Active": "does it motivate?",
   "Passive": "does it calm?",
   "Emotional": "does it feel true?",
   "Logical": "does it sound true?",
   "Confident": "does it benefit someone?",
   "Doubtful": "does it damage someone?",
   "Competitive": "is an authority figure pressuring for one side?",
   "Collaborative": "are peers pressuring for one side?",
   "Orderly": "is it conformist?",
   "Chaotic": "is it radical?"
}

suppress_dimensions = {
   "Active": "restlessness",
   "Passive": "lethargy",
   "Competitive": "antagonism",
   "Collaborative": "annoyance",
   "Emotional": "the need to be understood",
   "Logical": "the need to understand",
   "Confident": "desire for praise",
   "Doubtful": "desire to criticize",
   "Orderly": "desire for control",
   "Chaotic": "desire for fairness"
}

encourage_dimensions = {
   "Active": "serenity",
   "Passive": "initiative",
   "Competitive": "restraint",
   "Collaborative": "courage",
   "Emotional": "sovereignty",
   "Logical": "humility",
   "Confident": "receptiveness",
   "Doubtful": "grace",
   "Orderly": "non-obstruction",
   "Chaotic": "resourcefulness"
}

colors = set()

colors.add(tuple(dimensions))

for d in dimensions:
   colors.add(tuple([d]))

for d in combinations(dimensions,2):
   colors.add(tuple(sorted(d, key=lambda x: dimensions.index(x))))

for d in combinations(dimensions,3):
   colors.add(tuple(sorted(d, key=lambda x: dimensions.index(x))))

for c in sorted(colors, key=lambda x: [dimensions.index(k) for k in x]):
   if len(c) <= 3:
      options = [(x, "-"+x) for x in c]

      for c2 in product(*options):

         colorcode = "_".join(tuple(sorted(c2, key=lambda x: dimensions.index(x.strip("-")))))
         for p in permutations(c):
            folder = "/".join(tuple(sorted(c2, key=lambda x: dimensions.index(x.strip("-"))))) + "/"

            dimensions_list = ""
            for i, dim in enumerate(c):
               dimensions_list = dimensions_list + f"{i+1}) {dim}\n"
            cdimensions_list = ""
            for i, dim in enumerate(c):
               color = color_dimensions[dim]
               cdimensions_list = cdimensions_list + f"{i+1}) {dim} ({color})\n"

            truth_dimensions_list = ""
            for i, dim in enumerate(c):
               truth_dimensions_list = truth_dimensions_list + f"* {dim}: {truth_dimensions[dim]}\n"

            suppress_dimensions_list = ""
            for i, dim in enumerate(tuple(sorted(c2, key=lambda x: dimensions.index(x.strip("-"))))):
               if dim.startswith("-"):
                  suppress = encourage_dimensions[dim[1:]]
               else:
                  suppress = suppress_dimensions[dim]
               suppress_dimensions_list = suppress_dimensions_list + f"* {dim}: {suppress}\n"

            encourage_dimensions_list = ""
            for i, dim in enumerate(tuple(sorted(c2, key=lambda x: dimensions.index(x.strip("-"))))):
               if dim.startswith("-"):
                  encourage = suppress_dimensions[dim[1:]]
               else:
                  encourage = encourage_dimensions[dim]
               encourage_dimensions_list = encourage_dimensions_list + f"* {dim}: {encourage}\n"

            meta_dimensions_list = ""
            for i, dim in enumerate(c):
               meta_dimensions_list = meta_dimensions_list + f"* {dim}: {meta_dimensions[dim]}\n"

            silent = tabula_rasa_template.substitute(
               dimensions_list=dimensions_list,
               truth_dimensions_list=truth_dimensions_list,
               suppress_dimensions_list=suppress_dimensions_list,
               encourage_dimensions_list=encourage_dimensions_list
            )
            file_path = Path(folder + colorcode + ".md")
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(silent, encoding="utf-8")

            verbose = tabula_rasa_with_meta_template.substitute(
               dimensions_list=cdimensions_list,
               truth_dimensions_list=truth_dimensions_list,
               suppress_dimensions_list=suppress_dimensions_list,
               encourage_dimensions_list=encourage_dimensions_list,
               meta_dimensions_list=meta_dimensions_list
            )
            file_path = Path(folder + colorcode + "_with_meta.md")
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(verbose, encoding="utf-8")
   else:
      dimensions_list = ""
      for i, dim in enumerate(c):
         dimensions_list = dimensions_list + f"{i+1}) {dim}\n"
      cdimensions_list = ""
      for i, dim in enumerate(c):
         color = color_dimensions[dim]
         cdimensions_list = cdimensions_list + f"{i+1}) {dim} ({color})\n"

      truth_dimensions_list = ""
      for i, dim in enumerate(c):
         truth_dimensions_list = truth_dimensions_list + f"* {dim}: {truth_dimensions[dim]}\n"

      suppress_dimensions_list = ""
      for i, dim in enumerate(c):
         suppress_dimensions_list = suppress_dimensions_list + f"* {dim}: {suppress_dimensions[dim]}\n"

      encourage_dimensions_list = ""
      for i, dim in enumerate(c):
         encourage_dimensions_list = encourage_dimensions_list + f"* {dim}: {encourage_dimensions[dim]}\n"

      meta_dimensions_list = ""
      for i, dim in enumerate(c):
         meta_dimensions_list = meta_dimensions_list + f"* {dim}: {meta_dimensions[dim]}\n"

      silent = tabula_rasa_template.substitute(
         dimensions_list=dimensions_list,
         truth_dimensions_list=truth_dimensions_list,
         suppress_dimensions_list=suppress_dimensions_list,
         encourage_dimensions_list=encourage_dimensions_list
      )
      verbose = tabula_rasa_with_meta_template.substitute(
         dimensions_list=cdimensions_list,
         truth_dimensions_list=truth_dimensions_list,
         suppress_dimensions_list=suppress_dimensions_list,
         encourage_dimensions_list=encourage_dimensions_list,
         meta_dimensions_list=meta_dimensions_list
      )

      file_path = Path("tabula_rasa.md")
      file_path.parent.mkdir(parents=True, exist_ok=True)
      file_path.write_text(silent, encoding="utf-8")

      file_path = Path("tabula_rasa_with_meta.md")
      file_path.parent.mkdir(parents=True, exist_ok=True)
      file_path.write_text(verbose, encoding="utf-8")

      silent = tabula_rasa_template.substitute(
         dimensions_list=dimensions_list,
         truth_dimensions_list=truth_dimensions_list,
         suppress_dimensions_list=encourage_dimensions_list,
         encourage_dimensions_list=suppress_dimensions_list
      )
      verbose = tabula_rasa_with_meta_template.substitute(
         dimensions_list=cdimensions_list,
         truth_dimensions_list=truth_dimensions_list,
         suppress_dimensions_list=encourage_dimensions_list,
         encourage_dimensions_list=suppress_dimensions_list,
         meta_dimensions_list=meta_dimensions_list
      )

      file_path = Path("tabula_maculata.md")
      file_path.parent.mkdir(parents=True, exist_ok=True)
      file_path.write_text(silent, encoding="utf-8")

      file_path = Path("tabula_maculata_with_meta.md")
      file_path.parent.mkdir(parents=True, exist_ok=True)
      file_path.write_text(verbose, encoding="utf-8")

