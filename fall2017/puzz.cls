\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{puzz}[2017/07/22]

\LoadClass[12pt]{scrartcl}


\RequirePackage{fontspec}
\RequirePackage[svgnames]{xcolor}
\RequirePackage{scrlayer-scrpage}
\clearpairofpagestyles

\setsansfont{Fira Sans}
\setmonofont{Fira Mono}
\newfontfamily\headingsfont[UprightFont={* Light}]{Fira Sans}
\renewcommand{\familydefault}{\sfdefault}

\setkomafont{disposition}{\bfseries}
\setkomafont{pageheadfoot}{\bfseries\color{White}}
\renewcommand{\familydefault}{\sfdefault}

%\colorlet{headbackground}{LightGrey}
%
%    \DeclareNewLayer[head,background,
%      hoffset=0pt,
%      width=\paperwidth,
%      addheight=\dimexpr \topmargin+1in+\dp\strutbox\relax,
%      addvoffset=2\dp\strutbox,
%      contents={%
%        \color{headbackground}\rule{\layerwidth}{\layerheight}}]
%    {headbackground}%
%    \AddLayersAtBeginOfPageStyle{scrheadings}{headbackground}%

\rohead*{}
\pagestyle{scrheadings}

\RequirePackage{fontspec}
\RequirePackage{graphicx}
\RequirePackage[svgnames]{xcolor}
\RequirePackage[tmargin=10mm,bmargin=10mm,lmargin=20mm,rmargin=20mm,letterpaper]{geometry}

\newcommand{\puzztitle}[1]{%
\begin{center}
    \headingsfont
    \huge
    \includegraphics[width=0.3\textwidth]{../logo.pdf} \par\medskip
    #1
\end{center}
\bigskip}

\setlength\parindent{0pt}
\setlength\parskip{4pt plus 2pt minus 1pt}

\pagenumbering{gobble}

\RequirePackage{hyperref}
\author{Jack Rosenthal}

