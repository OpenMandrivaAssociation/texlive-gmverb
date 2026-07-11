%global tl_name gmverb
%global tl_revision 24288

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.98
Release:	%{tl_revision}.1
Summary:	A variant of LaTeX \verb, verbatim and shortvrb
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmverb
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A redefinition of \verb and verbatim so that long lines are breakable
before \ and after { with % as 'hyphen'. Allows you to define your own
verbatim-like environments (subject to a size limit) and allows you to
declare any single character as a shorthand as in the \MakeShortVerb
command of the shortvrb package of the LaTeX distribution. The package
depends on the gmutils package.

