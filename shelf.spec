#define snapshot 20220107

Name:		shelf
Version:	3.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Document and EBook collection manager
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/shelf/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitDocuments3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:	gettext
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:  pkgconfig(poppler-qt5)

Requires: mauikit-documents
Requires: qml(org.mauikit.texteditor)

%description
Document and EBook collection manager

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
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
