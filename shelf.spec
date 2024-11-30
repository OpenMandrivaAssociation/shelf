#define snapshot 20220107

Name:		shelf
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Document and EBook collection manager
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/shelf/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/maui-%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitDocuments4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:	gettext
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  pkgconfig(poppler-qt6)

Requires: mauikit-documents
Requires: qml(org.mauikit.texteditor)

%description
Document and EBook collection manager

%prep
%autosetup -p1 -n maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang shelf

%files -f shelf.lang
%{_bindir}/shelf
%{_datadir}/applications/org.kde.shelf.desktop
%{_datadir}/metainfo/org.kde.shelf.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/shelf.svg
