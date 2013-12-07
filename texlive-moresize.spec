# revision 17513
# category Package
# catalog-ctan /macros/latex/contrib/moresize
# catalog-date 2010-03-20 19:23:31 +0100
# catalog-license lppl
# catalog-version 1.9
Name:		texlive-moresize
Version:	1.9
Release:	6
Summary:	Allows font sizes up to 35.83pt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moresize
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moresize.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.9-2
+ Revision: 754106
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.9-1
+ Revision: 719062
- texlive-moresize
- texlive-moresize
- texlive-moresize
- texlive-moresize

