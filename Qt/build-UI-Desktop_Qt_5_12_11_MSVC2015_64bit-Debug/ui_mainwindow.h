/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.11
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *gridMain;
    QGridLayout *gridLayout;
    QTabWidget *tabWidget;
    QWidget *PI;
    QGridLayout *gridLayout_4;
    QGridLayout *PLgrid;
    QHBoxLayout *PIhorizontalBody;
    QScrollArea *PIleftScrollArea;
    QWidget *PIleftscrollAreaWidgetContents;
    QGridLayout *gridLayout_6;
    QVBoxLayout *PIleftverticalLayout;
    QSpacerItem *verticalSpacer_3;
    QFrame *line;
    QScrollArea *PIrightScrollArea;
    QWidget *PIrightscrollAreaWidgetContents;
    QGridLayout *gridLayout_5;
    QVBoxLayout *PIrightverticalLayout;
    QSpacerItem *verticalSpacer_2;
    QHBoxLayout *PIhorizontalTitle;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *PLallRun;
    QSpacerItem *horizontalSpacer_3;
    QFrame *line_2;
    QWidget *PD;
    QGridLayout *gridLayout_2;
    QHBoxLayout *PDhorizontalMain;
    QVBoxLayout *PDverticalMain;
    QHBoxLayout *PDtitel;
    QPushButton *PDnew;
    QPushButton *PDsave;
    QPushButton *PDload;
    QHBoxLayout *PDtitleadd;
    QSpacerItem *horizontalSpacer;
    QPushButton *PDadd;
    QScrollArea *scrollAreaNode;
    QWidget *scrollAreaWidgetContents;
    QGridLayout *gridLayout_3;
    QVBoxLayout *PDverticalNode;
    QSpacerItem *verticalSpacer;
    QWidget *PO;
    QGridLayout *gridLayout_9;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_11;
    QGridLayout *gridLayout_8;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QSpacerItem *verticalSpacer_4;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1200, 600);
        MainWindow->setMinimumSize(QSize(1200, 600));
        gridMain = new QWidget(MainWindow);
        gridMain->setObjectName(QString::fromUtf8("gridMain"));
        gridLayout = new QGridLayout(gridMain);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(7, 0, 7, 0);
        tabWidget = new QTabWidget(gridMain);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(2);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        QFont font;
        font.setPointSize(14);
        tabWidget->setFont(font);
        tabWidget->setLayoutDirection(Qt::LeftToRight);
        tabWidget->setTabPosition(QTabWidget::North);
        tabWidget->setTabShape(QTabWidget::Rounded);
        tabWidget->setElideMode(Qt::ElideMiddle);
        tabWidget->setUsesScrollButtons(true);
        tabWidget->setMovable(false);
        tabWidget->setTabBarAutoHide(false);
        PI = new QWidget();
        PI->setObjectName(QString::fromUtf8("PI"));
        gridLayout_4 = new QGridLayout(PI);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        PLgrid = new QGridLayout();
        PLgrid->setObjectName(QString::fromUtf8("PLgrid"));
        PIhorizontalBody = new QHBoxLayout();
        PIhorizontalBody->setObjectName(QString::fromUtf8("PIhorizontalBody"));
        PIleftScrollArea = new QScrollArea(PI);
        PIleftScrollArea->setObjectName(QString::fromUtf8("PIleftScrollArea"));
        PIleftScrollArea->setWidgetResizable(true);
        PIleftscrollAreaWidgetContents = new QWidget();
        PIleftscrollAreaWidgetContents->setObjectName(QString::fromUtf8("PIleftscrollAreaWidgetContents"));
        PIleftscrollAreaWidgetContents->setGeometry(QRect(0, 0, 771, 444));
        gridLayout_6 = new QGridLayout(PIleftscrollAreaWidgetContents);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        gridLayout_6->setContentsMargins(0, 11, 0, 0);
        PIleftverticalLayout = new QVBoxLayout();
        PIleftverticalLayout->setObjectName(QString::fromUtf8("PIleftverticalLayout"));
        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        PIleftverticalLayout->addItem(verticalSpacer_3);


        gridLayout_6->addLayout(PIleftverticalLayout, 0, 0, 1, 1);

        PIleftScrollArea->setWidget(PIleftscrollAreaWidgetContents);

        PIhorizontalBody->addWidget(PIleftScrollArea);

        line = new QFrame(PI);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        PIhorizontalBody->addWidget(line);

        PIrightScrollArea = new QScrollArea(PI);
        PIrightScrollArea->setObjectName(QString::fromUtf8("PIrightScrollArea"));
        PIrightScrollArea->setWidgetResizable(true);
        PIrightscrollAreaWidgetContents = new QWidget();
        PIrightscrollAreaWidgetContents->setObjectName(QString::fromUtf8("PIrightscrollAreaWidgetContents"));
        PIrightscrollAreaWidgetContents->setGeometry(QRect(0, 0, 384, 444));
        gridLayout_5 = new QGridLayout(PIrightscrollAreaWidgetContents);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        gridLayout_5->setContentsMargins(0, 11, 0, 0);
        PIrightverticalLayout = new QVBoxLayout();
        PIrightverticalLayout->setObjectName(QString::fromUtf8("PIrightverticalLayout"));
        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        PIrightverticalLayout->addItem(verticalSpacer_2);


        gridLayout_5->addLayout(PIrightverticalLayout, 0, 0, 1, 1);

        PIrightScrollArea->setWidget(PIrightscrollAreaWidgetContents);

        PIhorizontalBody->addWidget(PIrightScrollArea);

        PIhorizontalBody->setStretch(0, 2);
        PIhorizontalBody->setStretch(2, 1);

        PLgrid->addLayout(PIhorizontalBody, 2, 0, 1, 1);

        PIhorizontalTitle = new QHBoxLayout();
        PIhorizontalTitle->setObjectName(QString::fromUtf8("PIhorizontalTitle"));
        PIhorizontalTitle->setContentsMargins(-1, 7, -1, -1);
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        PIhorizontalTitle->addItem(horizontalSpacer_2);

        PLallRun = new QPushButton(PI);
        PLallRun->setObjectName(QString::fromUtf8("PLallRun"));
        QFont font1;
        font1.setPointSize(12);
        PLallRun->setFont(font1);

        PIhorizontalTitle->addWidget(PLallRun);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        PIhorizontalTitle->addItem(horizontalSpacer_3);


        PLgrid->addLayout(PIhorizontalTitle, 0, 0, 1, 1);

        line_2 = new QFrame(PI);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        PLgrid->addWidget(line_2, 1, 0, 1, 1);


        gridLayout_4->addLayout(PLgrid, 0, 0, 1, 1);

        tabWidget->addTab(PI, QString());
        PD = new QWidget();
        PD->setObjectName(QString::fromUtf8("PD"));
        gridLayout_2 = new QGridLayout(PD);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 11, 0, 0);
        PDhorizontalMain = new QHBoxLayout();
        PDhorizontalMain->setObjectName(QString::fromUtf8("PDhorizontalMain"));
        PDverticalMain = new QVBoxLayout();
        PDverticalMain->setObjectName(QString::fromUtf8("PDverticalMain"));
        PDtitel = new QHBoxLayout();
        PDtitel->setObjectName(QString::fromUtf8("PDtitel"));
        PDnew = new QPushButton(PD);
        PDnew->setObjectName(QString::fromUtf8("PDnew"));
        PDnew->setFont(font1);

        PDtitel->addWidget(PDnew);

        PDsave = new QPushButton(PD);
        PDsave->setObjectName(QString::fromUtf8("PDsave"));
        PDsave->setFont(font1);

        PDtitel->addWidget(PDsave);

        PDload = new QPushButton(PD);
        PDload->setObjectName(QString::fromUtf8("PDload"));
        PDload->setFont(font1);

        PDtitel->addWidget(PDload);


        PDverticalMain->addLayout(PDtitel);

        PDtitleadd = new QHBoxLayout();
        PDtitleadd->setObjectName(QString::fromUtf8("PDtitleadd"));
        PDtitleadd->setContentsMargins(-1, -1, 4, -1);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        PDtitleadd->addItem(horizontalSpacer);

        PDadd = new QPushButton(PD);
        PDadd->setObjectName(QString::fromUtf8("PDadd"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(PDadd->sizePolicy().hasHeightForWidth());
        PDadd->setSizePolicy(sizePolicy1);
        PDadd->setMinimumSize(QSize(35, 35));
        PDadd->setFont(font1);

        PDtitleadd->addWidget(PDadd);


        PDverticalMain->addLayout(PDtitleadd);

        scrollAreaNode = new QScrollArea(PD);
        scrollAreaNode->setObjectName(QString::fromUtf8("scrollAreaNode"));
        scrollAreaNode->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 1174, 405));
        gridLayout_3 = new QGridLayout(scrollAreaWidgetContents);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        PDverticalNode = new QVBoxLayout();
        PDverticalNode->setObjectName(QString::fromUtf8("PDverticalNode"));
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        PDverticalNode->addItem(verticalSpacer);


        gridLayout_3->addLayout(PDverticalNode, 3, 0, 1, 1);

        scrollAreaNode->setWidget(scrollAreaWidgetContents);

        PDverticalMain->addWidget(scrollAreaNode);


        PDhorizontalMain->addLayout(PDverticalMain);


        gridLayout_2->addLayout(PDhorizontalMain, 0, 0, 1, 1);

        tabWidget->addTab(PD, QString());
        PO = new QWidget();
        PO->setObjectName(QString::fromUtf8("PO"));
        gridLayout_9 = new QGridLayout(PO);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        groupBox = new QGroupBox(PO);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setFont(font1);
        gridLayout_11 = new QGridLayout(groupBox);
        gridLayout_11->setObjectName(QString::fromUtf8("gridLayout_11"));
        gridLayout_8 = new QGridLayout();
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        label->setFont(font1);

        gridLayout_8->addWidget(label, 0, 0, 1, 1);

        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setFont(font1);

        gridLayout_8->addWidget(label_2, 1, 0, 1, 1);

        lineEdit = new QLineEdit(groupBox);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setFont(font1);

        gridLayout_8->addWidget(lineEdit, 0, 1, 1, 1);

        lineEdit_2 = new QLineEdit(groupBox);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setFont(font1);

        gridLayout_8->addWidget(lineEdit_2, 1, 1, 1, 1);


        gridLayout_11->addLayout(gridLayout_8, 0, 0, 1, 1);


        gridLayout_9->addWidget(groupBox, 0, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_9->addItem(verticalSpacer_4, 1, 0, 1, 1);

        tabWidget->addTab(PO, QString());

        gridLayout->addWidget(tabWidget, 1, 0, 1, 1);

        MainWindow->setCentralWidget(gridMain);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1200, 26));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        PLallRun->setText(QApplication::translate("MainWindow", "\320\227\320\260\320\277\321\203\321\201\321\202\320\270\321\202\321\214 \320\262\321\201\321\221", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(PI), QApplication::translate("MainWindow", " \320\236\320\261\321\200\320\260\320\261\320\276\321\202\320\272\320\260 \320\270\320\267\320\276\320\261\321\200\320\260\320\266\320\265\320\275\320\270\320\271 ", nullptr));
        PDnew->setText(QApplication::translate("MainWindow", "\320\235\320\276\320\262\321\213\320\271 \320\277\321\200\320\276\321\204\320\270\320\273\321\214", nullptr));
        PDsave->setText(QApplication::translate("MainWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", nullptr));
        PDload->setText(QApplication::translate("MainWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214", nullptr));
        PDadd->setText(QApplication::translate("MainWindow", "+", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(PD), QApplication::translate("MainWindow", " \320\240\320\265\320\264\320\260\320\272\321\202\320\276\321\200 \320\277\321\200\320\276\321\204\320\270\320\273\321\217 \320\275\320\276\320\264\320\276\320\262 ", nullptr));
        groupBox->setTitle(QApplication::translate("MainWindow", "\320\236\320\261\321\211\320\270\320\265 \320\275\320\260\321\201\321\202\321\200\320\276\320\271\320\272\320\270", nullptr));
        label->setText(QApplication::translate("MainWindow", "\320\237\321\203\321\202\321\214 \320\264\320\276 meshroom.exe:", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "\320\237\321\203\321\202\321\214 \320\264\320\276 *.obj \320\264\320\273\321\217 3D:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(PO), QApplication::translate("MainWindow", " \320\235\320\260\321\201\321\202\321\200\320\276\320\271\320\272\320\270 ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
