class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        user_act_time = {}
        user_list = []
        # max_act_time = 0

        for user, act_time in logs:
            
            if user in user_act_time:
                user_log = user_act_time[user]
                if act_time not in user_log:
                    user_log.append(act_time)
                user_act_time[user] = user_log

            else:
                user_act_time[user] = [act_time]
                user_list.append(user)

            # max_act_time = max(max_act_time, act_time)

        ans = [0] * k

        for user in user_list:
            UAM = len(user_act_time[user])
            ans[UAM-1] += 1


        return ans
