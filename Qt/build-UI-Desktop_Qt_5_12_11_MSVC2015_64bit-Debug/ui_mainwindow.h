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
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *PDgridMain;
    QGridLayout *gridLayout;
    QHBoxLayout *PDhorizontalMain;
    QVBoxLayout *PDverticalMain;
    QHBoxLayout *PDtitel;
    QPushButton *PDnew;
    QPushButton *PDsave;
    QPushButton *PDload;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QHBoxLayout *PDtitleadd;
    QSpacerItem *horizontalSpacer;
    QPushButton *PDadd;
    QScrollArea *scrollAreaNode;
    QWidget *scrollAreaWidgetContents;
    QGridLayout *gridLayout_3;
    QVBoxLayout *PDverticalNode;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(757, 585);
        PDgridMain = new QWidget(MainWindow);
        PDgridMain->setObjectName(QString::fromUtf8("PDgridMain"));
        gridLayout = new QGridLayout(PDgridMain);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(7, 0, 7, 0);
        PDhorizontalMain = new QHBoxLayout();
        PDhorizontalMain->setObjectName(QString::fromUtf8("PDhorizontalMain"));
        PDverticalMain = new QVBoxLayout();
        PDverticalMain->setObjectName(QString::fromUtf8("PDverticalMain"));
        PDtitel = new QHBoxLayout();
        PDtitel->setObjectName(QString::fromUtf8("PDtitel"));
        PDnew = new QPushButton(PDgridMain);
        PDnew->setObjectName(QString::fromUtf8("PDnew"));
        QFont font;
        font.setPointSize(12);
        PDnew->setFont(font);

        PDtitel->addWidget(PDnew);

        PDsave = new QPushButton(PDgridMain);
        PDsave->setObjectName(QString::fromUtf8("PDsave"));
        PDsave->setFont(font);

        PDtitel->addWidget(PDsave);

        PDload = new QPushButton(PDgridMain);
        PDload->setObjectName(QString::fromUtf8("PDload"));
        PDload->setFont(font);

        PDtitel->addWidget(PDload);

        pushButton_2 = new QPushButton(PDgridMain);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy);
        pushButton_2->setFont(font);
        pushButton_2->setAutoRepeat(false);
        pushButton_2->setAutoExclusive(false);

        PDtitel->addWidget(pushButton_2);

        pushButton = new QPushButton(PDgridMain);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setFont(font);

        PDtitel->addWidget(pushButton);


        PDverticalMain->addLayout(PDtitel);

        PDtitleadd = new QHBoxLayout();
        PDtitleadd->setObjectName(QString::fromUtf8("PDtitleadd"));
        PDtitleadd->setContentsMargins(-1, -1, 4, -1);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        PDtitleadd->addItem(horizontalSpacer);

        PDadd = new QPushButton(PDgridMain);
        PDadd->setObjectName(QString::fromUtf8("PDadd"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(PDadd->sizePolicy().hasHeightForWidth());
        PDadd->setSizePolicy(sizePolicy1);
        PDadd->setMinimumSize(QSize(35, 35));
        PDadd->setFont(font);

        PDtitleadd->addWidget(PDadd);


        PDverticalMain->addLayout(PDtitleadd);

        scrollAreaNode = new QScrollArea(PDgridMain);
        scrollAreaNode->setObjectName(QString::fromUtf8("scrollAreaNode"));
        scrollAreaNode->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 737, 442));
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


        gridLayout->addLayout(PDhorizontalMain, 0, 0, 1, 1);

        MainWindow->setCentralWidget(PDgridMain);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 757, 26));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        PDnew->setText(QApplication::translate("MainWindow", "\320\235\320\276\320\262\321\213\320\271 \320\277\321\200\320\276\321\204\320\270\320\273\321\214", nullptr));
        PDsave->setText(QApplication::translate("MainWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", nullptr));
        PDload->setText(QApplication::translate("MainWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "Push", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "PushButton", nullptr));
        PDadd->setText(QApplication::translate("MainWindow", "+", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
