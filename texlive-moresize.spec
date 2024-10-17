Name:		texlive-moresize
Version:	17513
Release:	2
Summary:	Allows font sizes up to 35.83pt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moresize
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for using font sizes up to 35.88pt, for example with
the EC fonts. New commands \HUGE and \ssmall for selecting font
sizes are provided together with some options working around
current LaTeX2e shortcomings in using big font sizes. The
package also provides options for improving the typesetting of
paragraphs (or headlines) with embedded math expressions at
font sizes above 17.28pt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moresize/moresize.sty
%doc %{_texmfdistdir}/doc/latex/moresize/moresize.pdf
%doc %{_texmfdistdir}/doc/latex/moresize/moresize.upl
%doc %{_texmfdistdir}/doc/latex/moresize/msizetst.tex
#- source
%doc %{_texmfdistdir}/source/latex/moresize/moresize.dtx
%doc %{_texmfdistdir}/source/latex/moresize/moresize.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
