from manim import *
import numpy as np

class daa1(Scene):
	def construct(self):
		label1 = Text("An Overview of PageRank:")
		label2 = Text("its need, its working, and an example")

		label3 = Text("Muazzam Ali Kazmi")

		label1.scale(1.5)
		label1.shift(np.array([0,1,0]))
		label2.shift(np.array([0,0,0]))
		label3.shift(np.array([0,-2,0]))

		self.play(Write(label1))
		self.play(Write(label2))
		self.play(Write(label3))
		
		self.wait(2)

class daa2(Scene):
	def construct(self):
		goolag = TextMobject("Goolag", tex_to_color_map={"G": "#4285F4", "o": "#DB4437",  "g": "#4285F4", "l": "#0F9D58", "a": "#F4B400"})
        
		searchbox = Rectangle(fill_opacity=1.0, fill_color=WHITE, width=8, height=0.7)
		goolag.to_corner(UP*4)
		goolag.scale(2)
	
		button1 = Rectangle(fill_opacity=1.0, fill_color=WHITE, width=1.5, height=0.4)
		button1text = TextMobject("Goolag Search", fill_color=BLACK)
		button1text.scale(0.3)
		button1text.next_to(button1, ORIGIN)
		
		button2 = Rectangle(fill_opacity=1.0, fill_color=WHITE, width=1.5, height=0.4)
		button2.next_to(button1, RIGHT)
		button2text = TextMobject("I'm Feeling Lucky", fill_color=BLACK)
		button2text.scale(0.3)
		button2text.next_to(button2, ORIGIN)

		buttons = VGroup(button1, button2, button1text, button2text)
		buttons.next_to(searchbox, DOWN*3)
		
		self.play(Write(goolag), Write(searchbox), Write(button1), Write(button2), Write(button1text), Write(button2text))
		
				
		searchboxwithtext = VGroup(searchbox)
		
		#type some text
		sometext = "Muazzam"
		
		charmoblast = TextMobject("a")
		charmoblast.next_to(searchbox, LEFT)
		charmoblast.align_to(searchbox, LEFT)
		
		charmobs = []
		for i in sometext:
			charmob = TextMobject(i, fill_color=BLACK)
			charmob.scale(0.8)
			
			if (charmoblast):
				charmob.next_to(charmoblast, RIGHT*0.3)
				charmob.align_to(charmoblast, DOWN)
				
			searchboxwithtext.add(charmob)
			
			charmoblast = charmob.copy()
			
			self.play(Write(charmob),run_time=0.1)
		
		self.wait(1)
		
		self.play(Indicate(button1), Indicate(button1text))
		
		self.wait(1)
		
		charmoblast = TextMobject("a")
		charmoblast.scale(0.1)
		
		charmoblast.next_to(searchbox, LEFT)
		charmoblast.align_to(searchbox, LEFT)
				
		charmob = TextMobject(sometext, fill_color=BLACK)
		charmob.next_to(charmoblast, RIGHT)
		
		goolag2 = goolag.copy()
		goolag2.scale(0.4)
		
		goolag2.to_corner(UL*1.5)

		
		results = TextMobject("About 6,500,000 results (0.33 seconds)")
		
		self.play(FadeOut(buttons), Transform(goolag, goolag2), ApplyMethod(searchboxwithtext.to_corner, UP), FadeIn(results))
		
		results2 = results.copy()
		results2.next_to(goolag, DOWN)
		results2.scale(0.4)
		results2.align_to(goolag, LEFT)
		
		self.wait(1)
		self.play(Transform(results, results2))
		
		resrect1 = Rectangle(width=10.5, height=1)
		resrect1.next_to(results2, DOWN*2)
		resrect1.align_to(results2, LEFT)
		self.play(ShowCreation(resrect1), run_time=1)
		
		everything = VGroup(searchboxwithtext, goolag, resrect1, results)
		
		for i in range(10):
			resrect = Rectangle(width=10.5, height=1)
	
			if i<2:
				resrect.next_to(resrect1, DOWN*2)
				resrect.align_to(results2, LEFT)
			else:
				resrect.to_corner(DOWN*0.5)
				resrect.align_to(results2, LEFT)
				
			resrect1 = resrect.copy()
			
			everything.add(resrect)

			self.play(ShowCreation(resrect), run_time=0.5)
			
			if i > 2:
				self.play(ApplyMethod(everything.shift, UP*1.5), run_time=0.5)
			else:
				self.wait(0.5)
			
		
		notsoon = TextMobject("It's not going to stop anytime soon!")
		
		self.play(FadeOut(everything), FadeIn(notsoon))
		
		
		self.wait(1)
		
class daa3(Scene):
	def construct(self):
		
		notsoon = TextMobject("It's not going to stop anytime soon!")
		howrank = TextMobject("But... how do we rank relevant webpages at the top?", background_stroke_opacity=0.0, fill_color=WHITE, tex_to_color_map={"relevant:": YELLOW, "webpages": YELLOW})
		
		bypop = TextMobject("Solution: assess their popularity and authenticity", background_stroke_opacity=0.0, fill_color=WHITE, tex_to_color_map={"Solution:": RED})
		bypop.shift(DOWN)

		
		#pr = TextMobject("PageRank")
		#pr.scale(2)
		popPage = Circle()
		popPageT = TextMobject("Popular Page")
		popPageT.scale(0.5)
		popPageT.next_to(popPage, ORIGIN)
		
		self.add(notsoon)
		self.wait(1)
		
		self.play(Transform(notsoon, howrank))
		self.wait(2)
		self.play(FadeIn(bypop))
		self.wait(3)
		self.play(FadeOut(notsoon), FadeOut(bypop), GrowFromCenter(popPage), GrowFromCenter(popPageT))
		self.wait(1)
		
		everything = VGroup(popPage, popPageT)
		
		for i in range(10):
			myX = 3.0 * np.cos((TAU/10)*i)	#2.0 is radiuis, TAU is 2*pi
			myY = 3.0 * np.sin((TAU/10)*i)
			circ = Circle(fill_opacity=1.0, fill_color=RED)
			circ.scale(0.5)
			circT = TextMobject(("P" + str(i)), background_stroke_opacity=0.0, fill_color=WHITE)
			circT.scale(0.5)
			
			dotP = Dot(np.array([myX, myY, 0]))
			
			circ.next_to(dotP, ORIGIN)
			circT.next_to(dotP, ORIGIN)
			
			ptr1 = Arrow(dotP, np.array([myX*0.3, myY*0.3,0]))
			
			everything.add(ptr1, circ, circT)
			
			self.play(FadeIn(ptr1), GrowFromCenter(circ), GrowFromCenter(circT), run_time=0.2)
		
		self.wait(2)
		
		formula1 = TextMobject("$Pop(A) = P1 + P2 + P3 + ... + P_{N}$")
		formula1.to_corner(DOWN)
		
		formula2 = TextMobject(r"$Pop(A) = \sum_{i=1}^{N} P_{i}$")
		formula2.next_to(formula1, ORIGIN)
		
		self.play(ApplyMethod(everything.scale, 0.5))
		
		self.play(Write(formula1))
		self.wait(2)
		self.play(Transform(formula1, formula2))
		
		self.wait(2)
		
		wedef = TextMobject("We've created a ranking algorithm!", tex_to_color_map={"ranking algorithm!": YELLOW})
		wedef.to_corner(UP)
		
		self.play(FadeIn(wedef))
		
		self.wait(2)
		
		nopop = TextMobject(r"But... popularity $ \neq $ authenticity!", background_stroke_opacity=0.0, fill_color=YELLOW, tex_to_color_map={"But...": WHITE})
		nopop.shift(UP*1)
		
		self.play(FadeOut(everything), ApplyMethod(formula1.move_to, ORIGIN+DOWN*1), Transform(wedef, nopop))
		
		self.wait(1)
		
class daa4(Scene):
	def construct(self):
		nopop = TextMobject(r"But... popularity $ \neq $ authenticity!", background_stroke_opacity=0.0, fill_color=YELLOW, tex_to_color_map={"But...": WHITE})
		nopop.shift(UP*1)
		
		formula2 = TextMobject(r"$Pop(A) = \sum_{i=1}^{N} P_{i}$")
		formula2.move_to(DOWN)
		formula3 = TextMobject(r"$Pop(A) = \sum_{i=1}^{N} Pop(P_{i})$")
		formula3.next_to(formula2, ORIGIN)
		self.add(nopop)
		self.add(formula2)

		self.wait(4)
		
		recdef = TextMobject(r"Solution: recursive definition", background_stroke_opacity=0.0, fill_color=RED, tex_to_color_map={"recursive definition": WHITE})
		recdef.next_to(nopop, ORIGIN)
		
		self.wait(1)
		self.play(Transform(nopop, recdef))
		self.wait(2)
		
		self.play(Transform(formula2, formula3))
		self.wait(3)
		
		prob2 = TextMobject(r"But... some webpages just (like directories) link lots of pages!", background_stroke_opacity=0.0, fill_color=WHITE, tex_to_color_map={"webpages": YELLOW})
		prob2.next_to(nopop, ORIGIN)
		
		self.play(Transform(nopop, prob2))
		
		self.wait(2)

		sol2 = TextMobject(r"Solution: giving more weightage to smaller number of links",  background_stroke_opacity=0.0, fill_color=WHITE, tex_to_color_map={"Solution:": RED})
		
		formula4 = TextMobject(r"$Pop(A) = \sum_{i=1}^{N} \frac{Pop(P_{i})}{O(P_{i})}$")
		formula4.next_to(formula3, ORIGIN)
		
		formula4a = TextMobject(r"Where O(P) is the number of outgoing links from any page")
		formula4a.next_to(formula3, DOWN)
		formula4a.scale(0.7)
		
		sol2.next_to(nopop, ORIGIN)
		
		self.wait(2)
		
		self.play(Transform(nopop, sol2))
		
		self.wait(2)
		
		self.play(Transform(formula2, formula4))
		self.wait(1)
		
		self.play(FadeIn(formula4a))
		
		andthis = TextMobject(r"And... this is PageRank!", tex_to_color_map={"PageRank!": YELLOW})
		andthis.next_to(nopop, ORIGIN)
		
		self.wait(2)
		self.play(Transform(nopop, andthis))
		
		self.wait(3)
		
		italgo = TextMobject("PageRank is an iterative algorithm", tex_to_color_map={"iterative algorithm": YELLOW})
		italgo.next_to(nopop, ORIGIN)
		self.play(Transform(nopop, italgo), FadeOut(formula4a))
		
		self.wait(2)
		
		italgo2 = TextMobject("We stop the iterations when the PageRank values stop changing", tex_to_color_map={"iterations": YELLOW})
		italgo2.next_to(nopop, ORIGIN)
		self.play(Transform(nopop, italgo2))
		
		self.wait(2)
		
		italgo2 = TextMobject("For easier convergence, we add dampening factor, $d$", tex_to_color_map={"$d$": YELLOW})
		italgo2.next_to(nopop, ORIGIN)
		self.play(Transform(nopop, italgo2))
		
		self.wait(2)
		
		formula4 = TextMobject(r"$PR(A) = \frac{1-d}{N} + d \cdot \sum_{i=1}^{N} \frac{Pop(P_{i})}{O(P_{i})}$")
		formula4.next_to(formula3, ORIGIN)
		self.play(Transform(formula2, formula4))
		
		self.wait(3)
		
		self.play(FadeOut(formula2), FadeOut(nopop))
		
		self.wait(2)
		
		
		
class daa5(Scene):
	def construct(self):
		page1 = Rectangle(fill_opacity=1.0)
		page1a = Rectangle(fill_opacity=1.0, height=0.4, fill_color=BLACK, border_color=WHITE)

		label1 = TextMobject("Page B")
		label1.scale(0.4)
		label2 = TextMobject("Welcome! \\underline{Page D}", fill_color=BLACK, tex_to_color_map={"here": BLUE})
		label2.scale(0.5)

		labelA = TextMobject(r'\textless a href="A.html"\textgreater Page A\textless/a\textgreater', fill_color=BLACK)
		labelA.scale(0.4)
		labelB = TextMobject(r'\textless a href="B.html"\textgreater Page B\textless/a\textgreater', fill_color=BLACK)
		labelB.scale(0.4)
		labelC = TextMobject(r'\textless a href="C.html"\textgreater Page C\textless/a\textgreater', fill_color=BLACK)
		labelC.scale(0.4)
		labelD = TextMobject(r'\textless a href="D.html"\textgreater Page D\textless/a\textgreater', fill_color=BLACK)
		labelD.scale(0.4)

		fullpage = VGroup(page1, page1a, label1, label2)
		fullpage.arrange(np.array((0.,0.4,0.)))

		label1.next_to(page1a, ORIGIN)
		label2.next_to(page1,ORIGIN)
		
		self.play(FadeIn(page1a, UP), FadeIn(label1))
		self.play(Write(page1))
		self.play(FadeIn(label2))

		self.wait(1)
		self.play(ApplyMethod(fullpage.to_corner, np.array((3,1.,0.))))
		labelD.next_to(fullpage,ORIGIN)

		self.wait(0.5)
		self.play(Transform(label2, labelD))		
		
		#page D
		label1 = TextMobject("Page D")
		label1.scale(0.4)
		label1.next_to(page1a, ORIGIN)

		temppage = VGroup(page1, page1a, label1)

		fullpage3 = temppage.copy()

		fullpage3.next_to(fullpage, DOWN*5)
	
		#edge from B to D
		edgeBD = Arrow(fullpage.get_corner(DOWN), fullpage3.get_corner(UP), color=RED)
		self.play(GrowFromEdge(edgeBD, UP))
		self.wait()
		self.play(GrowFromCenter(fullpage3))
		
		#page C
		label1 = TextMobject("Page C")
		label1.scale(0.4)
		label1.next_to(page1a, ORIGIN)

		temppage = VGroup(page1, page1a, label1)

		fullpage4 = temppage.copy()

		fullpage4.next_to(fullpage, DOWN*5+LEFT*10)
		
		#link from B to C
		linkBC = labelC.copy().next_to(labelC.copy().next_to(fullpage,ORIGIN), DOWN)

		self.play(FadeIn(linkBC))

		#edge from B to C
		edgeBC = Arrow(fullpage.get_corner(DOWN), fullpage4.get_corner(UP+RIGHT), color=RED)
		self.play(GrowFromEdge(edgeBC, UP+RIGHT))
		self.wait()
		self.play(GrowFromCenter(fullpage4))

		#link from D to B
		linkDB = labelB.copy().next_to(fullpage3,ORIGIN)
		self.play(FadeIn(linkDB))
		#edge from D to B
		edgeDB = Arrow(fullpage3.get_corner(UP)-LEFT*0.5, fullpage.get_corner(DOWN)-LEFT*0.5, color=RED)
		self.play(GrowFromEdge(edgeDB, DOWN))


		#link from D to C
		linkDC = labelC.copy().next_to(labelB.copy().next_to(fullpage3,ORIGIN), DOWN)
		self.play(FadeIn(linkDC))
		#edge from D to C
		edgeDC = Arrow(fullpage3.get_corner(LEFT), fullpage4.get_corner(RIGHT), color=RED)
		self.play(GrowFromEdge(edgeDC, RIGHT))

		#page A
		label1 = TextMobject("Page A")
		label1.scale(0.4)
		label1.next_to(page1a, ORIGIN)

		temppage = VGroup(page1, page1a, label1)

		fullpage2 = temppage.copy()

		fullpage2.next_to(fullpage, LEFT*10)

		#link from C to A
		linkCA = labelA.copy().next_to(fullpage4,ORIGIN)
		self.play(FadeIn(linkCA))
		#edge from C to A
		edgeCA = Arrow(fullpage4.get_corner(UP), fullpage2.get_corner(DOWN), color=RED)
		self.play(GrowFromEdge(edgeCA, DOWN))
		self.wait()
		self.play(GrowFromCenter(fullpage2))
	

		#link from A to C
		linkAC = labelC.copy().next_to(fullpage2,ORIGIN)
		self.play(FadeIn(linkAC))

		#edge from A to C
		edgeAC = Arrow(fullpage2.get_corner(DOWN)+LEFT*0.5, fullpage4.get_corner(UP)+LEFT*0.5, color=RED)
		self.play(GrowFromEdge(edgeAC, UP))

		#self.play(ApplyMethod(fullpage.scale, 0.7))
		#self.play(ApplyMethod(fullpage2.scale, 0.7))
		#self.play(ApplyMethod(fullpage3.scale, 0.7))
		#self.play(ApplyMethod(fullpage4.scale, 0.7))
			
		
		#graph
		gnodeall = Rectangle(height=1.5, width=1.5)

		#nodes
		gnodeB = Circle(stroke_width=0)
		gnodeB.set_fill(YELLOW, opacity=1.0)
		gnodeB.next_to(gnodeall, RIGHT+UP)

		gnodeA = Circle(stroke_width=0)
		gnodeA.set_fill(YELLOW, opacity=1.0)
		gnodeA.next_to(gnodeall, LEFT+UP)

		gnodeD = Circle(stroke_width=0)
		gnodeD.set_fill(YELLOW, opacity=1.0)
		gnodeD.next_to(gnodeall, RIGHT+DOWN)

		gnodeC = Circle(stroke_width=0)
		gnodeC.set_fill(YELLOW, opacity=1.0)
		gnodeC.next_to(gnodeall, LEFT+DOWN)

		#labels of nodes
		gnodeBl = TextMobject("B", background_stroke_opacity=0.0, fill_color=RED)
		gnodeBl.scale(1.5)
		gnodeBl.next_to(gnodeB, ORIGIN)

		gnodeAl = TextMobject("A", background_stroke_opacity=0.0, fill_color=RED)
		gnodeAl.scale(1.5)
		gnodeAl.next_to(gnodeA, ORIGIN)

		gnodeCl = TextMobject("C", background_stroke_opacity=0.0, fill_color=RED)
		gnodeCl.scale(1.5)
		gnodeCl.next_to(gnodeC, ORIGIN)

		gnodeDl = TextMobject("D", background_stroke_opacity=0.0, fill_color=RED)
		gnodeDl.scale(1.5)
		gnodeDl.next_to(gnodeD, ORIGIN)

		#arrows
		edgeBC2 = Arrow(gnodeB.get_corner(DL), gnodeC.get_corner(UR), color=RED)
		edgeDB2 = Arrow(gnodeD.get_corner(UP)-0.2*LEFT, gnodeB.get_corner(DOWN)-0.2*LEFT, color=RED)
		edgeDC2 = Arrow(gnodeD.get_corner(LEFT), gnodeC.get_corner(RIGHT), color=RED)
		edgeCA2 = Arrow(gnodeC.get_corner(UP)-0.2*LEFT, gnodeA.get_corner(DOWN)-0.2*LEFT, color=RED)
		edgeAC2 = Arrow(gnodeA.get_corner(DOWN)+0.2*LEFT, gnodeC.get_corner(UP)+0.2*LEFT, color=RED)
		edgeBD2 = Arrow(gnodeB.get_corner(DOWN)+0.2*LEFT, gnodeD.get_corner(UP)+0.2*LEFT, color=RED)

		
		alllinks = VGroup(linkBC, linkDB, linkDC, linkCA, linkAC)
		alledges = VGroup(edgeBC, edgeDB, edgeDC, edgeCA, edgeAC, edgeBD)

		everything = VGroup(fullpage, fullpage2, fullpage3, fullpage4, alllinks, alledges)

		itsgraph = TextMobject("It is a graph!")
		itsgraph.scale(2)

		itsgraph.next_to(everything, DOWN)

		self.play(ApplyMethod(everything.scale, 0.8), Write(itsgraph))
		self.wait(1)

		self.play(Transform(fullpage, gnodeB), Transform(fullpage2, gnodeA), Transform(fullpage3, gnodeD), Transform(fullpage4, gnodeC), FadeOut(alllinks), Transform(edgeBC, edgeBC2), Transform(edgeDB, edgeDB2), Transform(edgeDC, edgeDC2), Transform(edgeCA, edgeCA2), Transform(edgeAC, edgeAC2), Transform(edgeBD, edgeBD2), GrowFromCenter(edgeBC2), GrowFromCenter(edgeDB2), GrowFromCenter(edgeDC2), GrowFromCenter(edgeCA2), GrowFromCenter(edgeAC2), GrowFromCenter(edgeBD2), GrowFromCenter(gnodeBl), GrowFromCenter(gnodeAl), GrowFromCenter(gnodeCl), GrowFromCenter(gnodeDl), FadeOut(itsgraph))

		self.wait(3)

class daa6(Scene):
	def construct(self):
		#graph
		gnodeall = Rectangle(height=1.5, width=1.5)

		#nodes
		gnodeB = Circle(stroke_width=0)
		gnodeB.set_fill(YELLOW, opacity=1.0)
		gnodeB.next_to(gnodeall, RIGHT+UP)

		gnodeA = Circle(stroke_width=0)
		gnodeA.set_fill(YELLOW, opacity=1.0)
		gnodeA.next_to(gnodeall, LEFT+UP)

		gnodeD = Circle(stroke_width=0)
		gnodeD.set_fill(YELLOW, opacity=1.0)
		gnodeD.next_to(gnodeall, RIGHT+DOWN)

		gnodeC = Circle(stroke_width=0)
		gnodeC.set_fill(YELLOW, opacity=1.0)
		gnodeC.next_to(gnodeall, LEFT+DOWN)

		#labels of nodes
		gnodeBl = TextMobject("B", background_stroke_opacity=0.0, fill_color=RED)
		gnodeBl.scale(1.5)
		gnodeBl.next_to(gnodeB, ORIGIN)

		gnodeAl = TextMobject("A", background_stroke_opacity=0.0, fill_color=RED)
		gnodeAl.scale(1.5)
		gnodeAl.next_to(gnodeA, ORIGIN)

		gnodeCl = TextMobject("C", background_stroke_opacity=0.0, fill_color=RED)
		gnodeCl.scale(1.5)
		gnodeCl.next_to(gnodeC, ORIGIN)

		gnodeDl = TextMobject("D", background_stroke_opacity=0.0, fill_color=RED)
		gnodeDl.scale(1.5)
		gnodeDl.next_to(gnodeD, ORIGIN)

		#arrows
		edgeBC2 = Arrow(gnodeB.get_corner(DL), gnodeC.get_corner(UR), color=RED)
		edgeDB2 = Arrow(gnodeD.get_corner(UP)-0.2*LEFT, gnodeB.get_corner(DOWN)-0.2*LEFT, color=RED)
		edgeDC2 = Arrow(gnodeD.get_corner(LEFT), gnodeC.get_corner(RIGHT), color=RED)
		edgeCA2 = Arrow(gnodeC.get_corner(UP)-0.2*LEFT, gnodeA.get_corner(DOWN)-0.2*LEFT, color=RED)
		edgeAC2 = Arrow(gnodeA.get_corner(DOWN)+0.2*LEFT, gnodeC.get_corner(UP)+0.2*LEFT, color=RED)
		edgeBD2 = Arrow(gnodeB.get_corner(DOWN)+0.2*LEFT, gnodeD.get_corner(UP)+0.2*LEFT, color=RED)

		
		fullgraph = VGroup(gnodeA, gnodeB, gnodeC, gnodeD, gnodeAl, gnodeBl, gnodeCl, gnodeDl, edgeBC2, edgeDB2, edgeDC2, edgeCA2, edgeAC2, edgeBD2)

		self.add(fullgraph)

		self.play(ApplyMethod(fullgraph.scale, 0.5))

		self.wait(1)

		self.play(ApplyMethod(fullgraph.to_corner, LEFT))

		matrix = TextMobject(r"$\begin{bmatrix} 0&0&1&0\\ 0&0&0&1\\ 1&1&0&1\\ 0&1&0&0\\ \end{bmatrix}$")
		matrix.shift(LEFT)
		
		self.play(Write(matrix))

		norT = TextMobject("Normalizing $\\rightarrow$");
		norT.scale(0.5)
		norT.next_to(matrix, UP)
		
		matrix2 = TextMobject(r"G = $\begin{bmatrix} 0&0&1&0\\ 0&0&0&0.5\\ 1&0.5&0&0.5\\ 0&0.5&0&0\\ \end{bmatrix}$")
		matrix2.next_to(matrix, RIGHT*2)
		
		self.wait(1)
		self.play(GrowFromEdge(norT, LEFT), FadeIn(matrix2))

		self.wait(1)
		
		self.play(FadeOut(norT), FadeOut(fullgraph), FadeOut(matrix), ApplyMethod(matrix2.to_corner, LEFT))
		
		self.wait(1)
		
class daa7(Scene):
	def construct(self):
		matrix2 = TextMobject(r"G = $\begin{bmatrix} 0&0&1&0\\ 0&0&0&0.5\\ 1&0.5&0&0.5\\ 0&0.5&0&0\\ \end{bmatrix}$")
		matrix2.to_corner(LEFT)

		
		initM = TextMobject("Initialzing PR (PageRank) vector by 1/N:")
		initM.to_corner(UP)
		
		matrix2 = TextMobject(r"G = $\begin{bmatrix} 0&0&1&0\\ 0&0&0&0.5\\ 1&0.5&0&0.5\\ 0&0.5&0&0\\ \end{bmatrix}$")
		matrix2.to_corner(LEFT)
		self.add(matrix2)

		matrix3 = TextMobject(r"G = $\begin{bmatrix} 0.21&0.21&1.06&0.21 \\ 0.21&0.21&0.21&0.64 \\ 1.06&0.64&0.21&0.64 \\ 0.21&0.64&0.21&0.21\\ \end{bmatrix}$")

		matrix3.to_corner(LEFT)


		self.wait(1)
		
		self.play(Write(initM))
		
		self.wait(1)
		
		vr1 = TextMobject(r"VR = $\begin{bmatrix} 0.25\\ 0.25\\ 0.25\\ 0.25\\ \end{bmatrix}$")
		self.play(Write(vr1))
		
		vr2 = TextMobject(r"VR = $\begin{bmatrix} 0.21&0.21&1.06&0.21 \\ 0.21&0.21&0.21&0.64 \\ 1.06&0.64&0.21&0.64 \\ 0.21&0.64&0.21&0.21\\ \end{bmatrix}$ $\cdot$  $\begin{bmatrix} 0.25\\ 0.25\\ 0.25\\ 0.25\\ \end{bmatrix}$")
		
		vrs = []
		
		
		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.25\\ 0.14375\\ 1\\ 0.14375\\ \end{bmatrix}$")
		vrs.append(vrnow)
		
		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.430625  \\ 0.09859375\\ 0.3721875 \\ 0.09859375\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.35385937\\ 0.07940234\\ 0.48733594\\ 0.07940234\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.45173555\\ 0.071246  \\ 0.40577246\\ 0.071246  \\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.38240659\\ 0.06777955\\ 0.48203431\\ 0.06777955\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.44722916\\ 0.06630631\\ 0.42015822\\ 0.06630631\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.39463449\\ 0.06568018\\ 0.47400515\\ 0.06568018\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.44040438\\ 0.06541408\\ 0.42876747\\ 0.06541408\\ \end{bmatrix}$")
		vrs.append(vrnow)
		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.40195235\\ 0.06530098\\ 0.46744569\\ 0.06530098\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.43068407\\ 0.06522381\\ 0.43886832\\ 0.06522381\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.41053807\\ 0.06522012\\ 0.45902169\\ 0.06522012\\ \end{bmatrix}$")
		vrs.append(vrnow)

		vrnow = TextMobject(r"$ = \begin{bmatrix} 0.42766844\\ 0.06521855\\ 0.44189446\\ 0.06521855\\ \end{bmatrix}$")
		vrs.append(vrnow)
		
		self.wait(1)

		damp1 = TextMobject("Dampening the matrix by: $\\frac{d}{n} + d \\cdot G$")
		damp1.next_to(initM, ORIGIN)

		vr1b = vr1.copy()
		vr1b.next_to(matrix3)

		self.play(Transform(matrix2, matrix3), Transform(initM, damp1), Transform(vr1, vr1b))

		self.wait(1)

		mulmat = TextMobject("Multiplying the garph with VR vector: ")
		mulmat.next_to(initM, ORIGIN)
		
		
		self.play(Transform(matrix2, vr2), Transform(initM, mulmat), FadeOut(vr1))
		
		self.wait(1)

		mulmat = TextMobject(r"It's the same as $\frac{1-d}{N} + d \cdot \sum_{i=1}^{N} \frac{Pop(P_{i})}{O(P_{i})}$", fill_color=YELLOW, tex_to_color_map={"It's the same as": WHITE})

		mulmat.next_to(initM, ORIGIN)
		self.play(Transform(initM, mulmat))

		self.wait(4)
		
		count = 0
		for i in vrs:
			count += 1
			itr1 = TextMobject(("Iteration " + str(count)), fill_color=YELLOW)
			

			i.to_corner(RIGHT)
			
			itr1.to_corner(UP)
			if count == 1:
				self.play(Transform(initM, itr1), FadeIn(i), ApplyMethod(matrix2.shift, LEFT*2))
			else:
				self.play(Transform(initM, itr1), Transform(vrs[0], i), run_time=(2.0/count))
			
	
		vrs[count-1].move_to(ORIGIN)
		
		self.wait(3)

		finalV = TextMobject(r"$\begin{bmatrix} PR(A)\\ PR(B)\\ PR(C)\\ PR(D)\\ \end{bmatrix} = \begin{bmatrix} 0.42766844\\ 0.06521855\\ 0.44189446\\ 0.06521855\\ \end{bmatrix}$")
		
		mulmat = TextMobject("And this is the PageRank of the nodes!", tex_to_color_map={"PageRank": YELLOW})
		mulmat.to_corner(UP)
		
		self.play(Transform(initM, mulmat), Transform(matrix2, finalV), FadeOut(vrs[0]))
		
		self.wait(10)
		
class daa8(Scene):
	def construct(self):
		questions = Text("Any questions?")		

		self.play(Write(questions))	
		self.wait(10)	
