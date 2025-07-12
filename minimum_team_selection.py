def smallest_sufficient_team(req_skills, people_skills):
    from collections import defaultdict

    skill_index = {skill: i for i, skill in enumerate(req_skills)}
    n = len(req_skills)
    
    people_mask = []
    for skills in people_skills:
        mask = 0
        for skill in skills:
            if skill in skill_index:
                mask |= 1 << skill_index[skill]
        people_mask.append(mask)
    
    dp = {0: []}  

    for i, p_mask in enumerate(people_mask):
        if p_mask == 0:
            continue

        for cur_mask, team in list(dp.items()):
            new_mask = cur_mask | p_mask
            if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                dp[new_mask] = team + [i]
    
    full_mask = (1 << n) - 1
    return dp[full_mask]
