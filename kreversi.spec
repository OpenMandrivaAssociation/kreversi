Summary:	Old reversi board game, also known as othello
Name:		kreversi
Version:	16.08.2
Release:	1
Epoch:		1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/kreversi/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	libkdegames-corebindings
Conflicts:	kdegames4-core < 1:4.9.80
BuildRequires:	cmake(KDEGames)
BuildRequires:	cmake(KDeclarative)
BuildRequires:	kdelibs-devel


%description
KReversi is a simple one player strategy game played against the computer.

If a player's piece is captured by an opposing player, that piece is turned
over to reveal the color of that player. A winner is declared when one player
has more pieces of his own color on the board and there are no more possible
moves.

%files
%{_bindir}/kreversi                                                                                    
%{_datadir}/applications/kde4/kreversi.desktop                                                         
%{_datadir}/apps/kreversi                                                                              
%{_iconsdir}/hicolor/*/apps/kreversi.png                                                               
%{_iconsdir}/oxygen/*/actions/lastmoves.*                                                              
%{_iconsdir}/oxygen/*/actions/legalmoves.*                                                             
%doc %{_docdir}/*/*/kreversi

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

