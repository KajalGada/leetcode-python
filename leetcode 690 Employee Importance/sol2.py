"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_map = {}

        for each_emp in employees:
            emp_map[each_emp.id] = each_emp

        tot_imp = 0
        list_emp = [id]

        while list_emp:

            cur_emp = list_emp.pop()
            tot_imp += emp_map[cur_emp].importance
            list_emp += emp_map[cur_emp].subordinates

        return tot_imp
