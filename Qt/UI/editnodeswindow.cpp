#include "editnodeswindow.h"
#include "ui_editnodeswindow.h"

EditNodesWindow::EditNodesWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::EditNodesWindow)
{
    ui->setupUi(this);
}

EditNodesWindow::~EditNodesWindow()
{
    delete ui;
}
