%global tl_name moresize
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Allows font sizes up to 35.83pt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moresize
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for using font sizes up to 35.88pt, for example with the EC
fonts. New commands \HUGE and \ssmall for selecting font sizes are
provided together with some options working around current LaTeX2e
shortcomings in using big font sizes. The package also provides options
for improving the typesetting of paragraphs (or headlines) with embedded
math expressions at font sizes above 17.28pt.

