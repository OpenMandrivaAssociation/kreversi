#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Old reversi board game, also known as othello
Name:		kreversi
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+ and LGPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/games/kreversi/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kreversi/-/archive/%{gitbranch}/kreversi-%{gitbranchd}.tar.bz2#/kreversi-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kreversi-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KDEGames6)

%rename plasma6-kreversi

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
%{_datadir}/knotifications6/*
%{_datadir}/metainfo/org.kde.kreversi.appdata.xml
%{_iconsdir}/*/*/apps/kreversi.png
%{_iconsdir}/*/*/actions/lastmoves.*
%{_iconsdir}/*/*/actions/legalmoves.*
