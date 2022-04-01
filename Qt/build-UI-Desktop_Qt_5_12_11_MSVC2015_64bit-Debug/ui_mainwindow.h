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
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *PDtitel;
    QPushButton *PDnew;
    QPushButton *PDsave;
    QPushButton *PDload;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QHBoxLayout *PDtitleadd;
    QSpacerItem *horizontalSpacer;
    QPushButton *PDadd;
    QFrame *frame;
    QGridLayout *gridLayout_2;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label;
    QPushButton *pushButton_7;
    QPushButton *pushButton_8;
    QPushButton *pushButton_9;
    QPushButton *pushButton_10;
    QSpacerItem *verticalSpacer;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(849, 527);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(7, 0, 7, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        PDtitel = new QHBoxLayout();
        PDtitel->setObjectName(QString::fromUtf8("PDtitel"));
        PDnew = new QPushButton(centralwidget);
        PDnew->setObjectName(QString::fromUtf8("PDnew"));
        QFont font;
        font.setPointSize(12);
        PDnew->setFont(font);

        PDtitel->addWidget(PDnew);

        PDsave = new QPushButton(centralwidget);
        PDsave->setObjectName(QString::fromUtf8("PDsave"));
        PDsave->setFont(font);

        PDtitel->addWidget(PDsave);

        PDload = new QPushButton(centralwidget);
        PDload->setObjectName(QString::fromUtf8("PDload"));
        PDload->setFont(font);

        PDtitel->addWidget(PDload);

        pushButton_2 = new QPushButton(centralwidget);
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

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setFont(font);

        PDtitel->addWidget(pushButton);


        verticalLayout->addLayout(PDtitel);

        PDtitleadd = new QHBoxLayout();
        PDtitleadd->setObjectName(QString::fromUtf8("PDtitleadd"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        PDtitleadd->addItem(horizontalSpacer);

        PDadd = new QPushButton(centralwidget);
        PDadd->setObjectName(QString::fromUtf8("PDadd"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(PDadd->sizePolicy().hasHeightForWidth());
        PDadd->setSizePolicy(sizePolicy1);
        PDadd->setMinimumSize(QSize(35, 35));
        PDadd->setFont(font);

        PDtitleadd->addWidget(PDadd);


        verticalLayout->addLayout(PDtitleadd);

        frame = new QFrame(centralwidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::Box);
        frame->setFrameShadow(QFrame::Raised);
        frame->setLineWidth(2);
        gridLayout_2 = new QGridLayout(frame);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, -1, 0, -1);
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setFont(font);

        horizontalLayout_4->addWidget(label);

        pushButton_7 = new QPushButton(frame);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        sizePolicy1.setHeightForWidth(pushButton_7->sizePolicy().hasHeightForWidth());
        pushButton_7->setSizePolicy(sizePolicy1);
        pushButton_7->setMinimumSize(QSize(35, 35));
        pushButton_7->setFont(font);

        horizontalLayout_4->addWidget(pushButton_7);

        pushButton_8 = new QPushButton(frame);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));
        sizePolicy1.setHeightForWidth(pushButton_8->sizePolicy().hasHeightForWidth());
        pushButton_8->setSizePolicy(sizePolicy1);
        pushButton_8->setMinimumSize(QSize(35, 35));
        pushButton_8->setFont(font);

        horizontalLayout_4->addWidget(pushButton_8);

        pushButton_9 = new QPushButton(frame);
        pushButton_9->setObjectName(QString::fromUtf8("pushButton_9"));
        sizePolicy1.setHeightForWidth(pushButton_9->sizePolicy().hasHeightForWidth());
        pushButton_9->setSizePolicy(sizePolicy1);
        pushButton_9->setMinimumSize(QSize(35, 35));
        pushButton_9->setFont(font);

        horizontalLayout_4->addWidget(pushButton_9);

        pushButton_10 = new QPushButton(frame);
        pushButton_10->setObjectName(QString::fromUtf8("pushButton_10"));
        sizePolicy1.setHeightForWidth(pushButton_10->sizePolicy().hasHeightForWidth());
        pushButton_10->setSizePolicy(sizePolicy1);
        pushButton_10->setMinimumSize(QSize(35, 35));
        pushButton_10->setFont(font);

        horizontalLayout_4->addWidget(pushButton_10);


        gridLayout_2->addLayout(horizontalLayout_4, 0, 0, 1, 1);


        verticalLayout->addWidget(frame);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        horizontalLayout->addLayout(verticalLayout);


        gridLayout->addLayout(horizontalLayout, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 849, 26));
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
        label->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        pushButton_7->setText(QApplication::translate("MainWindow", "^", nullptr));
        pushButton_8->setText(QApplication::translate("MainWindow", "v", nullptr));
        pushButton_9->setText(QApplication::translate("MainWindow", "R", nullptr));
        pushButton_10->setText(QApplication::translate("MainWindow", "-", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
