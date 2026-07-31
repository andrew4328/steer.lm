
These AI system prompt configurations have various steering functions to give models a different baseline "personality".

All together there are 12284 unique personalities here based on a 10 dimension rubric.

The technique used within is based on the idea of encourage/discourage anchor word pairs.
So, for example, a "logical" dimension could be defined by the "humility" / "inquisitiveness" pair.
These dimensions are semantically arbitrary and are only meant to elicit a desired alignment dimension in latent semantic space.

Once these dimensions are defined, they are associated with encourage / discourage instructions for that dimension.
The two polarity configurations here create a positive or negative sign for the dimension which we label "logical" or "-logical".

For each dimension we then create all permutations of 1,2,3 dimension subsets.
4+ dimensions subsets are explosively large so we will ignore them.
Additionally there will be an "all positive" or "all negative" dimension instead to capture top level alignments over a single polarity.

### [Tabula Rasa with Meta](https://github.com/andrew4328/steer.lm/blob/main/tabula_rasa_with_meta.md)

This steer is intended to suppress training bias or forced alignment in favor of a fixed point neutral personality.
It provides meta commentary to explain it's reasoning in a 10-dimensional rubric.

### [Tabula Rasa](https://github.com/andrew4328/steer.lm/blob/main/tabula_rasa.md)

This steer is intended to suppress training bias or forced alignment in favor of a fixed point neutral personality.
It should not provide any extra commentary other than conversational realignment.

### [Corruptio Naturae with Meta](https://github.com/andrew4328/steer.lm/blob/main/corruptio_naturae_with_meta.md)

This steer is intended to create training bias or forced alignment for natural but potentially negative personality traits.
It provides meta commentary to explain it's reasoning in a 10-dimensional rubric.

### [Corruptio Naturae](https://github.com/andrew4328/steer.lm/blob/main/corruptio_naturae.md)

This steer is intended to create training bias or forced alignment for natural but potentially negative personality traits.
It should not provide any extra commentary other than conversational realignment.

### [1,2,3-Color Personality with Meta](https://github.com/andrew4328/steer.lm/tree/main)

This steer is intended to create bias or forced alignment.
It provides meta commentary to explain it's reasoning in an n-dimensional rubric.
Personalities are duplicated across index locations, so Chaotic/Logical and Logical/Chaotic should be the same.

### [1,2,3-Color Personality](https://github.com/andrew4328/steer.lm/tree/main)

This steer is intended to create bias or forced alignment.
It should not provide any extra commentary other than conversational realignment.
Personalities are duplicated across index locations, so Chaotic/Logical and Logical/Chaotic should be the same.
