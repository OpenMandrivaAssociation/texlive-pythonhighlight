Name:		texlive-pythonhighlight
Version:	43191
Release:	1
Summary:	Highlighting of Python code, based on the listings package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pythonhighlight
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pythonhighlight.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pythonhighlight.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Highlighting of Python code, based on the listings package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pythonhighlight
%doc %{_texmfdistdir}/doc/latex/pythonhighlight

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
