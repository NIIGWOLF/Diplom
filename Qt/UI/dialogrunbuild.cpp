#include "dialogrunbuild.h"
#include "ui_dialogrunbuild.h"

DialogRunBuild::DialogRunBuild(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogRunBuild)
{
    ui->setupUi(this);
}

DialogRunBuild::~DialogRunBuild()
{
    delete ui;
}
