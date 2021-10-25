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
            emp_map[each_emp.id] = [each_emp.importance, each_emp.subordinates]
            
        emp_eval = [id]
        total_imp = 0
        
        while emp_eval:
            
            cur_emp = emp_eval.pop(0)
            total_imp += emp_map[cur_emp][0]
            emp_eval += emp_map[cur_emp][1]
            
        return total_imp
        
