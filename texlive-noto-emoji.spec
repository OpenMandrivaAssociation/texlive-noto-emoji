%global tl_name noto-emoji
%global tl_revision 62950

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.034
Release:	%{tl_revision}.1
Summary:	Noto Emoji fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/noto-emoji
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto-emoji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto-emoji.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Noto Color Emoji supports all emoji defined in the latest Unicode
version.

