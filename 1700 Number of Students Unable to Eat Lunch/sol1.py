class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # How many students want square and circular sandwich.
        sw_count = {}
        sw_count[1] = sum(students)
        sw_count[0] = len(students) - sw_count[1]

        # Does anyone want the top sandwich?
        for sw in sandwiches:

            # Reduce the num of students for top sandwich type
            if sw_count[sw]:
                sw_count[sw] -= 1

            # If no one wants the top sandwich, remaining students go hungry
            else:
                break

        return (sw_count[0] + sw_count[1])


            



