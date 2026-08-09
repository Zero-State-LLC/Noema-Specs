# Examples

Each JSON document is a complete wire message for `noema.core` version `1.0.0`.

| Example | Schema |
| --- | --- |
| `create-thought.command.json` | `../specs/command.schema.json` |
| `thought-created.event.json` | `../specs/event.schema.json` |
| `replay.request.json` | `../specs/replay-request.schema.json` |

The command and event share a correlation ID. The event's causation ID points to the command, while its event ID equals its envelope message ID. Replay positions are inclusive and preserve original global positions.
