# revision 24288
# category Package
# catalog-ctan /macros/latex/contrib/gmverb
# catalog-date 2011-10-14 16:42:22 +0200
# catalog-license lppl
# catalog-version v0.98
Name:		texlive-gmverb
Version:	v0.98
Release:	4
Summary:	A variant of LaTeX \verb, verbatim and shortvrb
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmverb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.98-2
+ Revision: 752364
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.98-1
+ Revision: 718568
- texlive-gmverb
- texlive-gmverb
- texlive-gmverb
- texlive-gmverb

