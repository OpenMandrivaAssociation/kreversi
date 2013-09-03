Name:		kreversi
Summary:	Old reversi board game, also known as othello
URL:		http://www.kde.org/applications/games/kreversi/
Version:	4.11.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Conflicts:	kdegames4-core < 1:4.9.80

%description
KReversi is a simple one player strategy game played against the computer.

If a player's piece is captured by an opposing player, that piece is turned
over to reveal the color of that player. A winner is declared when one player
has more pieces of his own color on the board and there are no more possible
moves.

%files
%{_kde_bindir}/kreversi
%{_kde_applicationsdir}/kreversi.desktop
%{_kde_appsdir}/kreversi
%{_kde_iconsdir}/hicolor/*/apps/kreversi.png
%{_kde_iconsdir}/oxygen/*/actions/lastmoves.*
%{_kde_iconsdir}/oxygen/*/actions/legalmoves.*
%{_kde_docdir}/*/*/kreversi

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package
- Some files from kdegames4-core should have been here
