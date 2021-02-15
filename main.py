def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Write your code here

        if (currentHusband is None):
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
        else:
            if herPreferences.index(he) <= herPreferences.index(currentHusband):
                unmarriedMen.append(currentHusband)
                menPreferences[currentHusband].pop(menPreferences[currentHusband].index(she))
                manSpouse[he] = she
                womanSpouse[she] = he
                unmarriedMen.remove(he)
            else:
                menPreferences[he].pop(menPreferences[he].index(she))
    return manSpouse


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # You might want to test your implementation on the following two tests:
    # assert (stableMatching(1, [[0]], [[0]]) == [0])
    # assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])

    if (
            stableMatching(
                4,
                [[0, 2, 1, 3], [1, 3, 0, 2], [2, 0, 1, 3], [0, 1, 2, 3]],
                [[2, 3, 1, 0], [2, 0, 3, 1], [1, 2, 3, 0], [2, 1, 0, 3]]
            )
            ==
            [1, 3, 2, 0]
    ):
        print("DEU CERTO")
    else:
        print("DEU ERRADO")
