# Programming Task

Write a parallelisable map / reduce function that will enable you to count the number of product recommendations a given product has, when given a list of product associations in the format below.

```json
{
  "generated": "2022-06-20T14:26:18.410244",
  "productRecommendations": {
    "AB290": ["AB389", "AB3882"],
    "AB399": ["AB3882", "AB500", "AB8339"]
    "AB3882": ["AB400", "AB399", "AB290", "AB190"]
    "AB190": ["AB3882"]
  }
}
```
E.g. AB3882 is recommended for AB290

The data needs to be split apart by a map function and appended to an intermediate data set.
Then the intermediate data set needs aggregating into a final data set with a reduce function.

These map reduce functional blocks should be independently parrallisable.

Develop the functional design using [TDD (Test Driven Development)](https://testdriven.io/blog/modern-tdd/). TDD should enable you to clearly articulate the desired functional requirements and then be certain that you have achieved the desired outcome.

