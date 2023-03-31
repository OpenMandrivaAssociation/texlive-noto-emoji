Name:		texlive-noto-emoji
Version:	62950
Release:	2
Summary:	Noto Emoji fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noto-emoji
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noto-emoji.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noto-emoji.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Noto Color Emoji supports all emoji defined in the latest
Unicode version.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/google/noto-emoji
%doc %{_texmfdistdir}/doc/fonts/noto-emoji

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
