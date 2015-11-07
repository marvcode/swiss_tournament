######################################################################
#
#  Written by: Marvin Fuller
#  Date: Oct 12, 2015
#  Filename: tournament_test.py
#  Purpose:
"""        The purpose of this module is an implementation of a
            Swiss-system tournament in python to interact with a PostgreSQL
            database.  This module will define all the functions needed
            to mange the tournament per the design rules of the project.
"""
#
######################################################################
# !/usr/bin/python
# -*- coding: utf-8 -*-

#   import libraries
from mftour import *
from pprint import pprint

player_count = countPlayers()


def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testplayerStandings():
    print playerStandings()


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before"
                         " they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 5:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1, draws1), (id2, name2, wins2, matches2, draw2)] = standings  # noqa
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "  # noqa
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."  # noqa


def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m, d) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")  # noqa
    print "7. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Hoyt Burne")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


def testRematchPrevention():
    deleteMatches()
    deletePlayers()
    registerPlayer("Tommy Hawk")
    registerPlayer("Brighton Early")
    registerPlayer("Brock Lee")
    registerPlayer("Cam Payne")
    registerPlayer('Tim Burr')
    registerPlayer('Willie Leak')
    registerPlayer('Owen Cash')
    registerPlayer('Walter Melon')
    reportMatch(1, 3)
    reportMatch(1, 4)
    reportMatch(3, 2)
    reportMatch(3, 5)
    reportMatch(2, 8)
    reportMatch(5, 6)
    reportMatch(7, 8)
    standings = playerStandings()
    pairings = swissPairings()
    pair1 = pairings[0]
    (player1,) = pair1[0:1]
    (player2,) = pair1[2:3]
    if (player1 == 3) and (player2 != 1):
        print "Extra Credit: Rematch Prevention Demonstrated.", \
              "\n   Players with matching scores were not paired since",\
              "\n   this could have caused a rematch scenario."
    else:
        print "Error in RematchPrevention function: "


def testDrawSupport():
    deleteMatches()
    deletePlayers()
    registerPlayer("Tommy Hawk")
    registerPlayer("Brighton Early")
    registerPlayer("Brock Lee")
    registerPlayer("Cam Payne")
    reportMatch(1, 3)
    reportMatch(2, 4)
    reportMatch(3, 2)
    reportDraw(1, 4)
    standings = playerStandings()
    (check1,) = (standings[0])[4:5]  # check the number of draws registered
    (check2,) = (standings[3])[4:5]  # check the number of draws registered
    if (check1 == 1) and (check2 == 1):
        print "Extra Credit: Support matches ending in Draws Demonstrated.", \
              "\n   Players with Draws are correctly shown in standings table."
    else:
        raise ValueError("Error in DrawSupport function: ")


if __name__ == '__main__':


    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    testRematchPrevention()
    testDrawSupport()
    print "\nSuccess!  All tests pass!"
