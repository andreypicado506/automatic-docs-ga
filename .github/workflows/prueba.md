## Hello World Action

### Inputs

| name | description | type | required | default |
| --- | --- | --- | --- | --- |
| `input1` | <p>The first input</p> | `string` | `true` | `First Input Value` |
| `input2` | <p>The second input</p> | `string` | `true` | `Second Input Value` |


### Usage

```yaml
jobs:
  job1:
    uses: ***PROJECT***@***VERSION***
    with:
      input1:
      # The first input
      #
      # Type: string
      # Required: true
      # Default: First Input Value

      input2:
      # The second input
      #
      # Type: string
      # Required: true
      # Default: Second Input Value
```



