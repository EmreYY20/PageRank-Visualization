from manim import *
import os
import random

class MainAnim(Scene):
    def construct(self):

        TEXT_SPEED = 0.045

        text_print = Text('print', color="#4ABCA5", font="Fira Code Retina")
        text_brac1 = Text('(', color=WHITE, font="Fira Code Retina")
        text_hello = Text('"hello world"', color="#CE9178", font="Fira Code Retina")
        text_brac2 = Text(')', color=WHITE, font="Fira Code Retina")
        text = VGroup(text_print,text_brac1,text_hello,text_brac2)
        for i in range(1,len(text)):
            text[i].next_to(text[i-1])
        text.center()
        #self.play(AddTextLetterByLetter(text, time_per_char = 0.5))
        self.play(Write(text,run_time=2))

        box = SurroundingRectangle(text, corner_radius=0.2)
        self.play(Create(box))
        self.play(box.animate.shift(UP),text.animate.shift(UP))
        sub = Text('The infamous hello world program in Python.\nPrints "hello world" onto the screen.\nYeah, that\'s it - sorry.', color=WHITE, font="Fira Code Retina", font_size=20)
        sub.move_to(box.get_bottom()  + DOWN * sub.height)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.remove(sub)
        self.play(Transform(box,SurroundingRectangle(text_print, corner_radius=0.2)))
        sub = Text('A pre-defined function we can use.\nPrint does exactly what the name implies.\nPrints stuff onto the screen.', color=WHITE, font="Fira Code Retina", font_size=20)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.remove(sub)
        sub = Text('We call or invoke a function with round brackets.', color=WHITE, font="Fira Code Retina", font_size=20)
        
        box2 = SurroundingRectangle(text_brac2, corner_radius=0.1)
        self.play(Transform(box,SurroundingRectangle(text_brac1, corner_radius=0.1)),Create(box2))
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(2)
        self.remove(sub,box2)
        sub = Text('Inside, we can write a literal string to be printed.\nWe need to surround it with quotation marks,\nlike "hello world" here.', color=WHITE, font="Fira Code Retina", font_size=20)
        self.play(Transform(box,SurroundingRectangle(text_hello, corner_radius=0.2)))
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.remove(sub)
        #self.play(FadeOut(text_hello))
        text_hello2 = Text('some_var', color="#9CDCFE", font="Fira Code Retina")
        text_hello3 = Text('5453.6', color="#B5CEA8", font="Fira Code Retina")
        text_hello2.move_to(text_hello)
        text_hello3.move_to(text_hello)
        self.play(Transform(text_hello,text_hello2))
        sub = Text('Or we could also print the contents of a variable.\nWe omit the quotation marks in this case.', color=WHITE, font="Fira Code Retina", font_size=20)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.remove(sub)
        self.play(Transform(text_hello,text_hello3))
        sub = Text('Or put a number inside the function.', color=WHITE, font="Fira Code Retina", font_size=20)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(2)
        self.remove(sub)
        self.play(FadeOut(text),FadeOut(box))
        sub = Text('The same concepts apply to other functions as well.\nThough they might have different and more parameters.', color=WHITE, font="Fira Code Retina", font_size=20)
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.wait(4)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        self.play(Write(Text("Happy Coding", font="Fira Code Retina")))
        self.wait(1)

            
            


if __name__ == "__main__":
    os.system(f"manim -pql {__file__} MainAnim")
    #os.system(f"manim -qh {__file__} MainAnim")