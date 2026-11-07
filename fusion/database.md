# Fusion Database (MongoDB)

## Collections
| Collection | Holds | Key fields |
|---|---|---|
| baseline | Expected result per checkpoint | `sid`, `tid`, checkpoint name, status, `expected` |
| | | |

## Relationships
- Scenario → task → script
- `sid` and `tid` are the MongoDB `_id` as hex text

## Execution results
- Run records and evidence used for healing
