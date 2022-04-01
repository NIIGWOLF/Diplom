/********************************************************************************
** Form generated from reading UI file 'editnodewindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.11
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_EDITNODEWINDOW_H
#define UI_EDITNODEWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_EditNodeWindow
{
public:
    QWidget *ENmain;
    QGridLayout *gridLayout_2;
    QGridLayout *ENmaingrid;
    QVBoxLayout *ENverticalmain;
    QFrame *ENTitle;
    QGridLayout *gridLayout_3;
    QHBoxLayout *ENverticalTitle;
    QLabel *ENltNameNode;
    QLineEdit *ENeNameNode;
    QPushButton *ENSave;
    QPushButton *ENLoad;
    QPushButton *ENLoadCMD;
    QPushButton *ENAddParam;
    QHBoxLayout *ENverticalPath;
    QLabel *ENltPathRun;
    QLineEdit *ENePathRun;
    QScrollArea *ENscrollAreaParam;
    QWidget *ENscrollAreaParamContents;
    QGridLayout *gridLayout_4;
    QGridLayout *ENgridParam;
    QPushButton *pushButton_6;
    QLineEdit *lineEdit_4;
    QLineEdit *lineEdit_3;
    QPushButton *pushButton_5;
    QLabel *ENltNameParam;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_5;
    QLabel *ENltValueParam;
    QLabel *label;
    QCheckBox *checkBox;
    QSpacerItem *ENverticalSpacer;
    QRadioButton *radioButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *EditNodeWindow)
    {
        if (EditNodeWindow->objectName().isEmpty())
            EditNodeWindow->setObjectName(QString::fromUtf8("EditNodeWindow"));
        EditNodeWindow->resize(800, 400);
        EditNodeWindow->setMinimumSize(QSize(800, 400));
        EditNodeWindow->setDockOptions(QMainWindow::AllowTabbedDocks|QMainWindow::AnimatedDocks);
        ENmain = new QWidget(EditNodeWindow);
        ENmain->setObjectName(QString::fromUtf8("ENmain"));
        gridLayout_2 = new QGridLayout(ENmain);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setHorizontalSpacing(7);
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        ENmaingrid = new QGridLayout();
        ENmaingrid->setSpacing(7);
        ENmaingrid->setObjectName(QString::fromUtf8("ENmaingrid"));
        ENverticalmain = new QVBoxLayout();
        ENverticalmain->setObjectName(QString::fromUtf8("ENverticalmain"));
        ENTitle = new QFrame(ENmain);
        ENTitle->setObjectName(QString::fromUtf8("ENTitle"));
        ENTitle->setFrameShape(QFrame::NoFrame);
        ENTitle->setFrameShadow(QFrame::Raised);
        gridLayout_3 = new QGridLayout(ENTitle);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        ENverticalTitle = new QHBoxLayout();
        ENverticalTitle->setObjectName(QString::fromUtf8("ENverticalTitle"));
        ENverticalTitle->setContentsMargins(-1, 10, -1, 10);
        ENltNameNode = new QLabel(ENTitle);
        ENltNameNode->setObjectName(QString::fromUtf8("ENltNameNode"));
        QFont font;
        font.setPointSize(12);
        ENltNameNode->setFont(font);

        ENverticalTitle->addWidget(ENltNameNode);

        ENeNameNode = new QLineEdit(ENTitle);
        ENeNameNode->setObjectName(QString::fromUtf8("ENeNameNode"));
        ENeNameNode->setMinimumSize(QSize(0, 35));
        ENeNameNode->setMaximumSize(QSize(16777215, 35));
        ENeNameNode->setFont(font);

        ENverticalTitle->addWidget(ENeNameNode);

        ENSave = new QPushButton(ENTitle);
        ENSave->setObjectName(QString::fromUtf8("ENSave"));
        ENSave->setMinimumSize(QSize(0, 35));
        ENSave->setMaximumSize(QSize(16777215, 35));
        QFont font1;
        font1.setPointSize(10);
        ENSave->setFont(font1);

        ENverticalTitle->addWidget(ENSave);

        ENLoad = new QPushButton(ENTitle);
        ENLoad->setObjectName(QString::fromUtf8("ENLoad"));
        ENLoad->setMinimumSize(QSize(0, 35));
        ENLoad->setMaximumSize(QSize(16777215, 35));
        ENLoad->setFont(font1);

        ENverticalTitle->addWidget(ENLoad);

        ENLoadCMD = new QPushButton(ENTitle);
        ENLoadCMD->setObjectName(QString::fromUtf8("ENLoadCMD"));
        ENLoadCMD->setMinimumSize(QSize(0, 35));
        ENLoadCMD->setMaximumSize(QSize(16777215, 35));
        ENLoadCMD->setFont(font1);

        ENverticalTitle->addWidget(ENLoadCMD);

        ENAddParam = new QPushButton(ENTitle);
        ENAddParam->setObjectName(QString::fromUtf8("ENAddParam"));
        ENAddParam->setMinimumSize(QSize(35, 35));
        ENAddParam->setMaximumSize(QSize(35, 35));
        ENAddParam->setFont(font1);

        ENverticalTitle->addWidget(ENAddParam);


        gridLayout_3->addLayout(ENverticalTitle, 1, 0, 1, 1);

        ENverticalPath = new QHBoxLayout();
        ENverticalPath->setObjectName(QString::fromUtf8("ENverticalPath"));
        ENltPathRun = new QLabel(ENTitle);
        ENltPathRun->setObjectName(QString::fromUtf8("ENltPathRun"));
        ENltPathRun->setFont(font);

        ENverticalPath->addWidget(ENltPathRun);

        ENePathRun = new QLineEdit(ENTitle);
        ENePathRun->setObjectName(QString::fromUtf8("ENePathRun"));
        ENePathRun->setMinimumSize(QSize(0, 35));
        ENePathRun->setMaximumSize(QSize(16777215, 35));
        ENePathRun->setFont(font);

        ENverticalPath->addWidget(ENePathRun);


        gridLayout_3->addLayout(ENverticalPath, 2, 0, 1, 1);


        ENverticalmain->addWidget(ENTitle);

        ENscrollAreaParam = new QScrollArea(ENmain);
        ENscrollAreaParam->setObjectName(QString::fromUtf8("ENscrollAreaParam"));
        ENscrollAreaParam->setWidgetResizable(true);
        ENscrollAreaParamContents = new QWidget();
        ENscrollAreaParamContents->setObjectName(QString::fromUtf8("ENscrollAreaParamContents"));
        ENscrollAreaParamContents->setGeometry(QRect(0, 0, 794, 215));
        gridLayout_4 = new QGridLayout(ENscrollAreaParamContents);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        ENgridParam = new QGridLayout();
        ENgridParam->setObjectName(QString::fromUtf8("ENgridParam"));
        pushButton_6 = new QPushButton(ENscrollAreaParamContents);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));
        pushButton_6->setMinimumSize(QSize(35, 35));
        pushButton_6->setMaximumSize(QSize(35, 35));

        ENgridParam->addWidget(pushButton_6, 2, 4, 1, 1);

        lineEdit_4 = new QLineEdit(ENscrollAreaParamContents);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));
        lineEdit_4->setMinimumSize(QSize(0, 35));
        lineEdit_4->setMaximumSize(QSize(16777215, 35));
        lineEdit_4->setFont(font);

        ENgridParam->addWidget(lineEdit_4, 2, 0, 1, 1);

        lineEdit_3 = new QLineEdit(ENscrollAreaParamContents);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));
        lineEdit_3->setMinimumSize(QSize(0, 35));
        lineEdit_3->setMaximumSize(QSize(16777215, 35));
        lineEdit_3->setFont(font);

        ENgridParam->addWidget(lineEdit_3, 1, 1, 1, 1);

        pushButton_5 = new QPushButton(ENscrollAreaParamContents);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton_5->sizePolicy().hasHeightForWidth());
        pushButton_5->setSizePolicy(sizePolicy);
        pushButton_5->setMinimumSize(QSize(35, 35));
        pushButton_5->setMaximumSize(QSize(35, 35));
        pushButton_5->setFont(font1);

        ENgridParam->addWidget(pushButton_5, 1, 4, 1, 1);

        ENltNameParam = new QLabel(ENscrollAreaParamContents);
        ENltNameParam->setObjectName(QString::fromUtf8("ENltNameParam"));
        ENltNameParam->setFont(font);

        ENgridParam->addWidget(ENltNameParam, 0, 0, 1, 1);

        lineEdit_2 = new QLineEdit(ENscrollAreaParamContents);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setMinimumSize(QSize(0, 35));
        lineEdit_2->setMaximumSize(QSize(16777215, 35));
        lineEdit_2->setFont(font);

        ENgridParam->addWidget(lineEdit_2, 1, 0, 1, 1);

        lineEdit_5 = new QLineEdit(ENscrollAreaParamContents);
        lineEdit_5->setObjectName(QString::fromUtf8("lineEdit_5"));
        lineEdit_5->setMinimumSize(QSize(0, 35));
        lineEdit_5->setMaximumSize(QSize(16777215, 35));
        lineEdit_5->setFont(font);

        ENgridParam->addWidget(lineEdit_5, 2, 1, 1, 1);

        ENltValueParam = new QLabel(ENscrollAreaParamContents);
        ENltValueParam->setObjectName(QString::fromUtf8("ENltValueParam"));
        ENltValueParam->setFont(font);

        ENgridParam->addWidget(ENltValueParam, 0, 1, 1, 1);

        label = new QLabel(ENscrollAreaParamContents);
        label->setObjectName(QString::fromUtf8("label"));

        ENgridParam->addWidget(label, 0, 3, 1, 1);

        checkBox = new QCheckBox(ENscrollAreaParamContents);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(checkBox->sizePolicy().hasHeightForWidth());
        checkBox->setSizePolicy(sizePolicy1);
        checkBox->setSizeIncrement(QSize(0, 0));
        checkBox->setBaseSize(QSize(0, 0));
        checkBox->setLayoutDirection(Qt::LeftToRight);
        checkBox->setCheckable(true);
        checkBox->setChecked(false);
        checkBox->setAutoRepeat(false);
        checkBox->setAutoExclusive(false);
        checkBox->setTristate(false);

        ENgridParam->addWidget(checkBox, 1, 3, 1, 1);

        ENgridParam->setColumnStretch(0, 1);
        ENgridParam->setColumnStretch(1, 2);

        gridLayout_4->addLayout(ENgridParam, 0, 0, 1, 1);

        ENverticalSpacer = new QSpacerItem(0, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_4->addItem(ENverticalSpacer, 3, 0, 1, 1);

        radioButton = new QRadioButton(ENscrollAreaParamContents);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));

        gridLayout_4->addWidget(radioButton, 4, 0, 1, 1);

        ENscrollAreaParam->setWidget(ENscrollAreaParamContents);

        ENverticalmain->addWidget(ENscrollAreaParam);


        ENmaingrid->addLayout(ENverticalmain, 2, 0, 1, 1);


        gridLayout_2->addLayout(ENmaingrid, 0, 0, 1, 1);

        EditNodeWindow->setCentralWidget(ENmain);
        menubar = new QMenuBar(EditNodeWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 26));
        EditNodeWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(EditNodeWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        EditNodeWindow->setStatusBar(statusbar);

        retranslateUi(EditNodeWindow);

        QMetaObject::connectSlotsByName(EditNodeWindow);
    } // setupUi

    void retranslateUi(QMainWindow *EditNodeWindow)
    {
        EditNodeWindow->setWindowTitle(QApplication::translate("EditNodeWindow", "\320\240\320\265\320\264\320\260\320\272\321\202\320\276\321\200 \320\275\320\276\320\264\320\276\320\262", nullptr));
        ENltNameNode->setText(QApplication::translate("EditNodeWindow", "\320\235\320\260\320\267\320\262\320\260\320\275\320\270\320\265 \320\275\320\276\320\264\320\260", nullptr));
        ENSave->setText(QApplication::translate("EditNodeWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", nullptr));
        ENLoad->setText(QApplication::translate("EditNodeWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214", nullptr));
        ENLoadCMD->setText(QApplication::translate("EditNodeWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214 cmd", nullptr));
        ENAddParam->setText(QApplication::translate("EditNodeWindow", "+", nullptr));
        ENltPathRun->setText(QApplication::translate("EditNodeWindow", "\320\237\321\203\321\202\321\214 \320\272 \320\270\321\201\320\277\320\276\320\273\320\275\321\217\320\265\320\274\320\276\320\274\321\203 \321\204\320\260\320\271\320\273\321\203", nullptr));
        pushButton_6->setText(QApplication::translate("EditNodeWindow", "-", nullptr));
        pushButton_5->setText(QApplication::translate("EditNodeWindow", "-", nullptr));
        ENltNameParam->setText(QApplication::translate("EditNodeWindow", "\320\235\320\260\320\267\320\262\320\260\320\275\320\270\320\265 \320\277\320\260\321\200\320\260\320\274\320\265\321\202\321\200\320\260", nullptr));
        ENltValueParam->setText(QApplication::translate("EditNodeWindow", "\320\227\320\275\320\260\321\207\320\265\320\275\320\270\320\265 \320\277\320\260\321\200\320\260\320\274\320\265\321\202\321\200\320\260", nullptr));
        label->setText(QApplication::translate("EditNodeWindow", "\320\237\320\276\320\272\320\260\320\267\320\260\321\202\321\214 \320\262 \320\261\321\213\321\201\321\202\321\200\320\276\320\274 \320\264\320\276\321\201\321\202\321\203\320\277\320\265", nullptr));
        checkBox->setText(QApplication::translate("EditNodeWindow", "\321\213\321\204\320\262", nullptr));
        radioButton->setText(QApplication::translate("EditNodeWindow", "RadioButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class EditNodeWindow: public Ui_EditNodeWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_EDITNODEWINDOW_H
