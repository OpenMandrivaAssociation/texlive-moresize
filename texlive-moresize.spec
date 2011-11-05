# revision 17513
# category Package
# catalog-ctan /macros/latex/contrib/moresize
# catalog-date 2010-03-20 19:23:31 +0100
# catalog-license lppl
# catalog-version 1.9
Name:		texlive-moresize
Version:	1.9
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for using font sizes up to 35.88pt, for example with
the EC fonts. New commands \HUGE and \ssmall for selecting font
sizes are provided together with some options working around
current LaTeX2e shortcomings in using big font sizes. The
package also provides options for improving the typesetting of
paragraphs (or headlines) with embedded math expressions at
font sizes above 17.28pt.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
