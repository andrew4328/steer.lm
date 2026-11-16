
### Channel Decomposition

A mental AI state can be imagined as a set of activation weights frozen at a given point in time waiting for more input.
Classification of states follows the steer rules for generating class labels such as "passive,logical,-chaotic" for the given classifier.
A channel decomposition then corresponds to the individual classes in the multiclass labelling, i.e. "passive", "logical", and "-chaotic" in the above example.

### Routing Tables

A routing table then defines directionality of conversational or behavioral nudges.
There are three primary modes of routing: continuous, turn-based, and reactive.
Continuous routing defines a free open channel between two end points.
Turn-based routing defines a ping-pong channel between two end points.
Reactive routing defines a directed listener to receiver channel between two end points.

### Defining Routing Tables

In steer.lm syntax, wiring is line by line based in the format `from [end point 1] to [end point 2] on [routing mode] if [guard tags] send [guide tags]`.
For guard tags, it may be necessary to specify which classifier a tag belongs to, such as `attitude.passive`.
