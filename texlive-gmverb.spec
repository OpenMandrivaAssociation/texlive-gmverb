Name:		texlive-gmverb
Version:	24288
Release:	2
Summary:	A variant of LaTeX \verb, verbatim and shortvrb
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmverb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A redefinition of \verb and verbatim so that long lines are
breakable before \ and after { with % as 'hyphen'. Allows you
to define your own verbatim-like environments (subject to a
size limit) and allows you to declare any single character as a
shorthand as in the \MakeShortVerb command of the shortvrb
package of the LaTeX distribution. The package depends on the
gmutils package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmverb/gmverb.sty
%doc %{_texmfdistdir}/doc/latex/gmverb/README
%doc %{_texmfdistdir}/doc/latex/gmverb/gmverb.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
