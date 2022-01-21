# aws_cdk_testing_python
I'll demo how to TDD and testing using aws cdk for python.

### Cheat Sheet
* Template methods [`Match` API is accepted as an argument]:
    * It's for the following cloudformation's
      template sections: _Resources_, _Outputs_, 
      _Mappings_ and _Parameters_
      * _has__* : Asserts.
      * _find__* : Finds and returns matching.

* Capture methods [`Match` API is accepted as an argument]:
    * _as_* : Returns captured value
    * next: Multiple capturing, get the next value from iterator
### Youtube videos.
1. [AWS CDK Testing (Python | TDD) - I](https://www.youtube.com/watch?v=aYlZJgDO3SY)
2. [AWS CDK Testing (Python | TDD) - II](https://www.youtube.com/watch?v=dYgewTMIBQ8)