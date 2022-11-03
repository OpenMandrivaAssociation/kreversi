%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Old reversi board game, also known as othello
Name:		kreversi
Version:	22.08.3
Release:	1
Epoch:		1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/kreversi/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDEGames)

%description
KReversi is a simple one player strategy game played against the computer.

If a player's piece is captured by an opposing player, that piece is turned
over to reveal the color of that player. A winner is declared when one player
has more pieces of his own color on the board and there are no more possible
moves.

%files -f %{name}.lang
%{_bindir}/kreversi
%{_datadir}/applications/org.kde.kreversi.desktop
%{_datadir}/kreversi
%{_datadir}/knotifications5/*
%{_datadir}/metainfo/org.kde.kreversi.appdata.xml
%{_iconsdir}/*/*/apps/kreversi.png
%{_iconsdir}/*/*/actions/lastmoves.*
%{_iconsdir}/*/*/actions/legalmoves.*
#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
