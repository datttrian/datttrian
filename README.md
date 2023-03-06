# Getting Started

- Remove the repository if exists
- Clone the repository from Github
- Switch to the directory
- Create & activate virtualenv
- Install requirements
- Fix imports
- Check code style
- Run tests

```bash
rm -rf codility
git clone https://github.com/datttrian/codility
cd codility
pyenv virtualenv-delete --force codility && pyenv install 3.11 --skip-existing && pyenv virtualenv `pyenv latest 3.11` codility && pyenv local codility && pyenv && activate codility
pip install -r requirements.txt
isort .
bash style.sh
pytest
```

# Codility

Python solutions to the training exercises and tests at https://codility.com/programmers/lessons/

1. Iterations
    * BinaryGap
1. Arrays
    * CyclicRotation
    * OddOccurrencesInArray
1. Time Complexity
    * FrogJmp
    * PermMissingElem
    * TapeEquilibrium
1. Counting Elements
    * FrogRiverOne
    * PermCheck
    * MaxCounters
    * MissingInteger
1. Prefix Sums
    * PassingCars
    * CountDiv
    * GenomicRangeQuery
    * MinAvgTwoSlice
1. Sorting
    * Distinct
    * MaxProductOfThree
    * Triangle
    * NumberOfDiscIntersections
1. Stacks and Queues
    * Brackets
    * Fish
    * Nesting
    * StoneWall
1. Leader
    * Dominator
    * EquiLeader
1. Maximum slice problem
    * MaxProfit
    * MaxSliceSum
    * MaxDoubleSliceSum
1. Prime and composite numbers
    * CountFactors
    * MinPerimeterRectangle
    * Flags
    * Peaks
1. Sieve of Eratosthenes
    * CountNonDivisible
    * CountSemiprimes
1. Euclidean algorithm
    * ChocolatesByNumbers
    * CommonPrimeDivisors
1. Fibonacci numbers
    * FibFrog
    * Ladder
1. Binary search algorithm
    * MinMaxDivision
    * NailingPlanks
1. Caterpillar method
    * AbsDistinct
    * CountDistinctSlices
    * CountTriangles
    * MinAbsSumOfTwo
1. Greedy algorithms
    * MaxNonoverlappingSegments
    * TieRopes
1. Dynamic programming
    * NumberSolitaire
    * MinAbsSum
