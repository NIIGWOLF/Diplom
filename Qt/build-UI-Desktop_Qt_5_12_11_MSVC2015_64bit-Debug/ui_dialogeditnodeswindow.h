/********************************************************************************
** Form generated from reading UI file 'dialogeditnodeswindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.11
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOGEDITNODESWINDOW_H
#define UI_DIALOGEDITNODESWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_DialogEditNodesWindow
{
public:
    QGridLayout *gridLayout;
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
    QSpacerItem *ENverticalSpacer;
    QGridLayout *ENgridParam;
    QLabel *ENltValueParam;
    QLabel *ENltBool;
    QLabel *ENltNameParam;
    QLabel *ENltDelButton;
    QHBoxLayout *ENhorizontalSaveChanged;
    QSpacerItem *horizontalSpacer;
    QPushButton *ENSaveChanged;

    void setupUi(QDialog *DialogEditNodesWindow)
    {
        if (DialogEditNodesWindow->objectName().isEmpty())
            DialogEditNodesWindow->setObjectName(QString::fromUtf8("DialogEditNodesWindow"));
        DialogEditNodesWindow->resize(800, 400);
        DialogEditNodesWindow->setMinimumSize(QSize(800, 400));
        gridLayout = new QGridLayout(DialogEditNodesWindow);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        ENmaingrid = new QGridLayout();
        ENmaingrid->setSpacing(7);
        ENmaingrid->setObjectName(QString::fromUtf8("ENmaingrid"));
        ENverticalmain = new QVBoxLayout();
        ENverticalmain->setObjectName(QString::fromUtf8("ENverticalmain"));
        ENTitle = new QFrame(DialogEditNodesWindow);
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

        ENscrollAreaParam = new QScrollArea(DialogEditNodesWindow);
        ENscrollAreaParam->setObjectName(QString::fromUtf8("ENscrollAreaParam"));
        ENscrollAreaParam->setWidgetResizable(true);
        ENscrollAreaParamContents = new QWidget();
        ENscrollAreaParamContents->setObjectName(QString::fromUtf8("ENscrollAreaParamContents"));
        ENscrollAreaParamContents->setGeometry(QRect(0, 0, 772, 200));
        gridLayout_4 = new QGridLayout(ENscrollAreaParamContents);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        ENverticalSpacer = new QSpacerItem(0, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_4->addItem(ENverticalSpacer, 3, 0, 1, 1);

        ENgridParam = new QGridLayout();
        ENgridParam->setObjectName(QString::fromUtf8("ENgridParam"));
        ENltValueParam = new QLabel(ENscrollAreaParamContents);
        ENltValueParam->setObjectName(QString::fromUtf8("ENltValueParam"));
        ENltValueParam->setFont(font);

        ENgridParam->addWidget(ENltValueParam, 0, 1, 1, 1);

        ENltBool = new QLabel(ENscrollAreaParamContents);
        ENltBool->setObjectName(QString::fromUtf8("ENltBool"));
        ENltBool->setFont(font);
        ENltBool->setAlignment(Qt::AlignCenter);
        ENltBool->setWordWrap(true);

        ENgridParam->addWidget(ENltBool, 0, 2, 1, 1);

        ENltNameParam = new QLabel(ENscrollAreaParamContents);
        ENltNameParam->setObjectName(QString::fromUtf8("ENltNameParam"));
        ENltNameParam->setFont(font);

        ENgridParam->addWidget(ENltNameParam, 0, 0, 1, 1);

        ENltDelButton = new QLabel(ENscrollAreaParamContents);
        ENltDelButton->setObjectName(QString::fromUtf8("ENltDelButton"));

        ENgridParam->addWidget(ENltDelButton, 0, 3, 1, 1);

        ENgridParam->setColumnStretch(0, 1);
        ENgridParam->setColumnStretch(1, 2);

        gridLayout_4->addLayout(ENgridParam, 0, 0, 1, 1);

        ENscrollAreaParam->setWidget(ENscrollAreaParamContents);

        ENverticalmain->addWidget(ENscrollAreaParam);


        ENmaingrid->addLayout(ENverticalmain, 2, 0, 1, 1);


        gridLayout->addLayout(ENmaingrid, 0, 0, 1, 1);

        ENhorizontalSaveChanged = new QHBoxLayout();
        ENhorizontalSaveChanged->setObjectName(QString::fromUtf8("ENhorizontalSaveChanged"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        ENhorizontalSaveChanged->addItem(horizontalSpacer);

        ENSaveChanged = new QPushButton(DialogEditNodesWindow);
        ENSaveChanged->setObjectName(QString::fromUtf8("ENSaveChanged"));
        ENSaveChanged->setMinimumSize(QSize(0, 35));
        ENSaveChanged->setFont(font1);

        ENhorizontalSaveChanged->addWidget(ENSaveChanged);


        gridLayout->addLayout(ENhorizontalSaveChanged, 1, 0, 1, 1);


        retranslateUi(DialogEditNodesWindow);

        QMetaObject::connectSlotsByName(DialogEditNodesWindow);
    } // setupUi

    void retranslateUi(QDialog *DialogEditNodesWindow)
    {
        DialogEditNodesWindow->setWindowTitle(QApplication::translate("DialogEditNodesWindow", "\320\240\320\265\320\264\320\260\320\272\321\202\320\276\321\200 \320\275\320\276\320\264\320\276\320\262", nullptr));
        ENltNameNode->setText(QApplication::translate("DialogEditNodesWindow", "\320\235\320\260\320\267\320\262\320\260\320\275\320\270\320\265 \320\275\320\276\320\264\320\260", nullptr));
        ENSave->setText(QApplication::translate("DialogEditNodesWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", nullptr));
        ENLoad->setText(QApplication::translate("DialogEditNodesWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214", nullptr));
        ENLoadCMD->setText(QApplication::translate("DialogEditNodesWindow", "\320\227\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214 cmd", nullptr));
        ENAddParam->setText(QApplication::translate("DialogEditNodesWindow", "+", nullptr));
        ENltPathRun->setText(QApplication::translate("DialogEditNodesWindow", "\320\237\321\203\321\202\321\214 \320\272 \320\270\321\201\320\277\320\276\320\273\320\275\321\217\320\265\320\274\320\276\320\274\321\203 \321\204\320\260\320\271\320\273\321\203", nullptr));
        ENltValueParam->setText(QApplication::translate("DialogEditNodesWindow", "\320\227\320\275\320\260\321\207\320\265\320\275\320\270\320\265 \320\277\320\260\321\200\320\260\320\274\320\265\321\202\321\200\320\260", nullptr));
        ENltBool->setText(QApplication::translate("DialogEditNodesWindow", "\320\221\321\213\321\201\321\202\321\200\321\213\320\271 \320\264\320\276\321\201\321\202\321\203\320\277", nullptr));
        ENltNameParam->setText(QApplication::translate("DialogEditNodesWindow", "\320\235\320\260\320\267\320\262\320\260\320\275\320\270\320\265 \320\277\320\260\321\200\320\260\320\274\320\265\321\202\321\200\320\260", nullptr));
        ENltDelButton->setText(QString());
        ENSaveChanged->setText(QApplication::translate("DialogEditNodesWindow", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214 \320\270\320\267\320\274\320\265\320\275\320\265\320\275\320\270\321\217", nullptr));
    } // retranslateUi

};

namespace Ui {
    class DialogEditNodesWindow: public Ui_DialogEditNodesWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOGEDITNODESWINDOW_H
