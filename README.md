# ListRevFunctions

Using this package you can perform opertions on two lists with second list reversed.

## INDEX

- [ListRevFunctions](#listrevfunctions)
  - [INDEX](#index)
  - [Installation](#installation)
  - [Usage](#usage)
- [Functions](#functions)
  - [1. Addition](#1-addition)
  - [2. Subtraction](#2-subtraction)
  - [3. Multiplication](#3-multiplication)
  - [4. Division](#4-division)
  - [5. Modulus](#5-modulus)
  - [6. Power](#6-power)
  - [7. Floor Division](#7-floor-division)
  - [8. and\_](#8-and_)
  - [9. or\_](#9-or_)

## Installation

```bash
pip install ListRevFunctions
```

## Usage

Declaration of class perform


```python
import ListOperations as lo #importing package
list1 = [4,5,7]
list2 = [1,2,3]
ob = lo.perform() #creating object for class perform
```

# Functions

## 1. Addition

```python
ob.add()  #function for addition Output will be [7, 7, 8]
```

## 2. Subtraction

```python
ob.sub()  #function for subtraction Output will be [3, 3, 4]
```

## 3. Multiplication

```python
ob.mul()  #function for multiplication Output will be [4, 10, 21]
```

## 4. Division

```python
ob.div()  #function for division Output will be [4.0, 2.5, 2.3333333333333335]
```

## 5. Modulus

```python
ob.mod()  #function for modulus Output will be [0, 1, 1]
```

## 6. Power

```python
ob.pow()  #function for power Output will be [4, 25, 343]
```

## 7. Floor Division

```python
ob.floordiv()  #function for floor division Output will be [4, 2, 2]
```

## 8. and_

```python
ob.and_()  #function returns the first false value if there are any output will be [1, 2,3]
```

## 9. or_

```python
ob.or_()  #function returns the first true value if there are any output will be [4, 5, 7]
```
