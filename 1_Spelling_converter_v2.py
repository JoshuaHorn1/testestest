"""Spelling converter v2"""
import easygui

nz_word = easygui.enterbox("Please enter the NZ word/phrase.", "Word to check").lower()
if "our" in nz_word:
    us_word = nz_word.replace("our", "or")
    easygui.msgbox(f"The American spelling of {nz_word} is ", "Result")
elif "ise" in nz_word:
    us_word = nz_word.replace("ise", "ize")
    easygui.msgbox(f"The American spelling of {nz_word} is ", "Result")
elif "yse" in nz_word:
    us_word = nz_word.replace("yse", "yze")
    easygui.msgbox(f"The American spelling of {nz_word} is {us_word}", "Result")
else:
    easygui.msgbox("No spelling changed.", "No change")
