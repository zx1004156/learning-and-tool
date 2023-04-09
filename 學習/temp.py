from bs4 import BeautifulSoup

html = ''' 
<!DOCTYPE html>
<!-- saved from url=(0072)https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php -->
<html lang="en" data-darkreader-mode="dynamic" data-darkreader-scheme="dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style class="darkreader darkreader--fallback" media="screen"></style><style class="darkreader darkreader--text" media="screen"></style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, #bit-notification-bar-iframe, ::-webkit-calendar-picker-indicator {
    filter: invert(100%) hue-rotate(180deg) contrast(90%) !important;
}</style><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}</style><style class="darkreader darkreader--variables" media="screen">:root {
   --darkreader-neutral-background: #131516;
   --darkreader-neutral-text: #d8d4cf;
   --darkreader-selection-background: #004daa;
   --darkreader-selection-text: #e8e6e3;
}</style><style class="darkreader darkreader--root-vars" media="screen"></style><style class="darkreader darkreader--user-agent" media="screen">html {
    background-color: #181a1b !important;
}
html {
    color-scheme: dark !important;
}
html, body {
    background-color: #181a1b;
}
html, body {
    border-color: #736b5e;
    color: #e8e6e3;
}
a {
    color: #3391ff;
}
table {
    border-color: #545b5e;
}
::placeholder {
    color: #b2aba1;
}
input:-webkit-autofill,
textarea:-webkit-autofill,
select:-webkit-autofill {
    background-color: #404400 !important;
    color: #e8e6e3 !important;
}
::-webkit-scrollbar {
    background-color: #202324;
    color: #aba499;
}
::-webkit-scrollbar-thumb {
    background-color: #454a4d;
}
::-webkit-scrollbar-thumb:hover {
    background-color: #575e62;
}
::-webkit-scrollbar-thumb:active {
    background-color: #484e51;
}
::-webkit-scrollbar-corner {
    background-color: #181a1b;
}
::selection {
    background-color: #004daa !important;
    color: #e8e6e3 !important;
}
::-moz-selection {
    background-color: #004daa !important;
    color: #e8e6e3 !important;
}</style>

    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <meta http-equiv="Access-Control-Allow-Origin" content="*">

    <title>TBCCoin 後台管理系統</title>

    <!-- Custom fonts for this template-->
    <link href="./TBCCoin 後台管理系統_files/all.min.css" rel="stylesheet" type="text/css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link href="./TBCCoin 後台管理系統_files/css.css" rel="stylesheet"><style class="darkreader darkreader--sync" media="screen"></style>
    
    <!-- Custom styles for this template-->
    <link href="./TBCCoin 後台管理系統_files/sb-admin-2.min.css" rel="stylesheet"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" type="text/css" href="./TBCCoin 後台管理系統_files/datatables.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="./TBCCoin 後台管理系統_files/jquery-ui.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="./TBCCoin 後台管理系統_files/jquery.fancybox.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    
    <link rel="stylesheet" type="text/css" href="./TBCCoin 後台管理系統_files/bootstrap-switch.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link href="./TBCCoin 後台管理系統_files/search_title.css" rel="stylesheet"><style class="darkreader darkreader--sync" media="screen"></style>

    <!-- Bootstrap core JavaScript-->
    <script src="./TBCCoin 後台管理系統_files/jquery.min.js.下載"></script><meta name="darkreader" content="9743d742a7c54890a5dcbe9de6a14078"><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: #7b5300 !important;
    border-color: #d8b013 !important;
    color: #f3e8c8 !important;
}
::placeholder {
    opacity: 0.5 !important;
}
#edge-translate-panel-body,
.MuiTypography-body1,
.nfe-quote-text {
    color: var(--darkreader-neutral-text) !important;
}
gr-main-header {
    background-color: #0f3a48 !important;
}
.tou-z65h9k,
.tou-mignzq,
.tou-1b6i2ox,
.tou-lnqlqk {
    background-color: var(--darkreader-neutral-background) !important;
}
.tou-75mvi {
    background-color: #032029 !important;
}
.tou-ta9e87,
.tou-1w3fhi0,
.tou-1b8t2us,
.tou-py7lfi,
.tou-1lpmd9d,
.tou-1frrtv8,
.tou-17ezmgn {
    background-color: #0a0a0a !important;
}
.tou-uknfeu {
    background-color: #231603 !important;
}
.tou-6i3zyv {
    background-color: #19576c !important;
}
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }</style>
    <script src="./TBCCoin 後台管理系統_files/bootstrap.bundle.min.js.下載"></script>
    <script src="./TBCCoin 後台管理系統_files/bootstrap-switch.js.下載" data-turbolinks-track="true"></script>
    <!-- Core plugin JavaScript-->
    <script src="./TBCCoin 後台管理系統_files/jquery.easing.min.js.下載"></script>

    <!-- Custom scripts for all pages-->
    <script type="text/javascript" src="./TBCCoin 後台管理系統_files/datatables.min.js.下載"></script>
    
    <script src="./TBCCoin 後台管理系統_files/jquery-ui.min.js.下載"></script>
    <script src="./TBCCoin 後台管理系統_files/jquery.fancybox.min.js.下載"></script>

    <style>
    .dt-buttons{
        float: right;
    }
    </style><style class="darkreader darkreader--sync" media="screen"></style>
</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/index.php">
                <div class="sidebar-brand-icon rotate-n-15">
                    <i class="fas fa-wallet"></i>
                </div>
                <div class="sidebar-brand-text mx-3">TBCCoin</div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <!-- <li class="nav-item ">
                <a class="nav-link" href="./index.php">
                <i class="fas fa-fw fa-tachometer-alt"></i>
                <span>首頁</span></a>
            </li> -->

            <!-- Divider -->
            <hr class="sidebar-divider">
                                                <div class="sidebar-heading">
                系統            </div>
                        <li class="nav-item ">
                <a class="nav-link" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/asset_management.php">
                    <i class="fas fa-fw fa-table"></i>
                    <span>幣別管理</span></a>
            </li>
                                    <div class="sidebar-heading">
                商家請款            </div>
                        <li class="nav-item active">
                <a class="nav-link" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php">
                    <i class="fas fa-fw fa-table"></i>
                    <span>商家請款管理</span></a>
            </li>
                                    <div class="sidebar-heading">
                收款二維碼            </div>
                        <li class="nav-item ">
                <a class="nav-link" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/receive_student.php">
                    <i class="fas fa-fw fa-table"></i>
                    <span>收款二維碼</span></a>
            </li>
                                    <!-- Divider -->
            <hr class="sidebar-divider d-none d-md-block">

            <!-- Sidebar Toggler (Sidebar) -->
            <div class="text-center d-none d-md-inline">
                <button class="rounded-circle border-0" id="sidebarToggle"></button>
            </div>

        </ul>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

                    <!-- Sidebar Toggle (Topbar) -->
                    <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
                        <i class="fa fa-bars"></i>
                    </button>

                    <!-- Topbar Search -->


                    <!-- Topbar Navbar -->
                    <ul class="navbar-nav ml-auto">

                        <!-- Nav Item - Search Dropdown (Visible Only XS) -->
                 



                        <div class="topbar-divider d-none d-sm-block"></div>

                        <!-- Nav Item - User Information -->
                        <li class="nav-item dropdown no-arrow">
                            <a class="nav-link dropdown-toggle" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <span class="mr-2 d-none d-lg-inline text-gray-600 small">信東幣核銷</span>
                                <i class="fas fa-user fa-sm fa-fw mr-2 text-dark-400"></i>
                            </a>
                            <!-- Dropdown - User Information -->
                            <div class="dropdown-menu dropdown-menu-right shadow animated--grow-in" aria-labelledby="userDropdown">
                                <!-- <a class="dropdown-item" href="#">
                  <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
                  Profile
                </a>
                <a class="dropdown-item" href="#">
                  <i class="fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"></i>
                  Settings
                </a>
                <a class="dropdown-item" href="#">
                  <i class="fas fa-list fa-sm fa-fw mr-2 text-gray-400"></i>
                  Activity Log
                </a> -->
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#" data-toggle="modal" data-target="#logoutModal">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                    登出
                                </a>
                            </div>
                        </li>

                    </ul>

                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <form method="POST" enctype="multipart/form-data" class="teacher_form" action="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php">
    <div class="row">
        <div class="col-12">
            <div class="alert alert_global alert-danger" role="alert" style="display:none">
            </div>
        </div>
    </div>
    <input type="hidden" name="loading_enable" id="loading_enable" value="Y">

    <div class="row">
        <div class="col-12">
            身分：
            <select name="ftype" id="ftype">
                <option value="">請選擇身分</option>
                <option value="POS">商家</option>
            </select>
            對象：
            <select name="ftarget" id="ftarget"><option value="">請選擇對象</option><option value="0986077323">群祐(0986077323)</option><option value="0986269079">盈養園(0986269079)</option><option value="0986817628">百麗診所(0986817628)</option><option value="acc88@sintong.com">信東流通NG商店(acc88@sintong.com)</option><option value="custservice@sintong.com">信東銷管部(銷售)(custservice@sintong.com)</option><option value="finance@aimedicine.com.tw">麥迪森醫藥(finance@aimedicine.com.tw)</option><option value="investment@sintong.com">禾健生技(investment@sintong.com)</option><option value="patty@gp-corp.com">健裕生技(patty@gp-corp.com)</option><option value="pos001@vteamsystem.com">商家測試(pos001@vteamsystem.com)</option><option value="s82910g@sintong.com">健康商店(s82910g@sintong.com)</option><option value="S999999999">系統回收(S999999999)</option><option value="yiting@taiwanvpc.com.tw">榮民員購商店(yiting@taiwanvpc.com.tw)</option><option value="zoesun@sintong.com">紹善醫療(zoesun@sintong.com)</option></select>
            &nbsp;&nbsp;
            日期區間：
            <input type="text" name="fsdate" id="fsdate" value="" autocomplete="off" class="hasDatepicker">
            &nbsp;&nbsp;-&nbsp;&nbsp;
            <input type="text" name="fedate" id="fedate" value="" autocomplete="off" class="hasDatepicker">
            &nbsp;&nbsp;
            款項狀態：
            <select name="fstatus" id="fstatus">
                <option value="">請選擇款項狀態</option>
                <option value="C">
                    已請款
                </option>
                <option value="Y">
                    未請款
                </option>
            </select>
            &nbsp;&nbsp;
            幣別：
            <select name="currency" id="currency">
                <option value="">請選擇幣別</option>
                                <option value="5">
                    信東幣                </option>
                                <option value="7">
                    盈養園幣                </option>
                            </select>
            <input class="btn btn-primary" type="button" value="查詢" id="search_btn">
        </div>
        <hr style="width:100%">
    </div>
</form>


<div class="row ">
    <div class="col-12">
        <form method="POST" enctype="multipart/form-data" class="edit_form" action="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/check_invoice.php">
            <input type="hidden" name="ser_type" value="POS">
            <input type="hidden" name="ser_target" value="yiting@taiwanvpc.com.tw">
            <input type="hidden" name="ser_sdate" value="2023-02-01">
            <input type="hidden" name="ser_edate" value="2023-02-28">
            <input type="hidden" name="ser_status" value="C">
            <input type="hidden" name="options" value="">

            <div id="example_wrapper" class="dataTables_wrapper dt-bootstrap4 no-footer"><div class="dt-buttons btn-group">      <button class="btn btn-secondary buttons-print btn-primary" tabindex="0" aria-controls="example" type="button"><span>列印</span></button> <button class="btn btn-secondary buttons-excel buttons-html5 btn-info" tabindex="0" aria-controls="example" type="button"><span>儲存成Excel</span></button> <button class="btn btn-secondary" tabindex="0" aria-controls="example" type="button"><span>請款預覽</span></button> <button class="btn btn-secondary" tabindex="0" aria-controls="example" type="button"><span>廠商請款單預覽</span></button> </div><div id="example_processing" class="dataTables_processing card" style="display: none;">處理中</div><table id="example" class="table table-striped table-bordered dataTable no-footer dtr-inline" style="width: 100%;" role="grid" aria-describedby="example_info"><thead>
                    <tr role="row"><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 49.8px;"><input type="checkbox" name="check_all" onclick="CheckAll()">全選</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 69.8px;">交易序號</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 52.8px;">對象</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 113.8px;">身分</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 169.8px;">時間</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 52.8px;">狀態</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 52.8px;">幣別</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 42.8px;">金額</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 170.8px;">請款執行人</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 170px;">請款執行時間</th></tr>
                </thead>
                
            <tbody><tr role="row" class="odd"><td tabindex="0"></td><td>11360</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-06 15:53:52</td><td>已請款</td><td>信東幣</td><td>1200</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="even"><td tabindex="0"></td><td>11336</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-06 11:37:44</td><td>已請款</td><td>信東幣</td><td>300</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="odd"><td tabindex="0"></td><td>11334</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-06 11:21:08</td><td>已請款</td><td>信東幣</td><td>2700</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="even"><td tabindex="0"></td><td>11323</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-06 10:13:06</td><td>已請款</td><td>信東幣</td><td>3000</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="odd"><td tabindex="0"></td><td>11322</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-06 10:11:56</td><td>已請款</td><td>信東幣</td><td>900</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="even"><td tabindex="0"></td><td>11312</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-04 10:44:55</td><td>已請款</td><td>信東幣</td><td>600</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="odd"><td tabindex="0"></td><td>11311</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-04 10:41:55</td><td>已請款</td><td>信東幣</td><td>900</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="even"><td tabindex="0"></td><td>11270</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-02 15:51:37</td><td>已請款</td><td>信東幣</td><td>1500</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="odd"><td tabindex="0"></td><td>11269</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-02 15:49:20</td><td>已請款</td><td>信東幣</td><td>900</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr><tr role="row" class="even"><td tabindex="0"></td><td>11259</td><td>蕭怡婷</td><td>員工(一般會員)</td><td>2023-02-02 08:50:33</td><td>已請款</td><td>信東幣</td><td>2250</td><td>信東幣核銷(STfinance)</td><td>2023-03-01 09:02:12</td></tr></tbody></table><div class="dataTables_info" id="example_info" role="status" aria-live="polite"></div></div>
        </form>
    </div>
    <script type="text/javascript">
        function CheckAll() {
            var ck = document.getElementsByName("someName[]");
            var flag = $("input[name='check_all']").prop("checked");
            for (var i = 0; i < ck.length; i++)
                ck[i].checked = flag;
        }
        $(function () {
            $("select[name='fstatus']").change(function () {
                if ($(this).val() != "") {
                    $(".alert_global").hide();
                }
            });
            $("input[name='fsdate']").change(function () {
                if ($(this).val() != "") {
                    $(".alert_global").hide();
                }
            });
            $("input[name='fedate']").change(function () {
                if ($(this).val() != "") {
                    $(".alert_global").hide();
                }
            });
            $("input[name='fsdate']").datepicker({
                changeMonth: true,
                changeYear: true,
                dateFormat: "yy-mm-dd"
            });
            $("input[name='fedate']").datepicker({
                changeMonth: true,
                changeYear: true,
                dateFormat: "yy-mm-dd"
            });

            $("select[name='ftype']").change(function () {
                if ($(this).val() != "") {
                    $("select[name='ftarget']").empty().append(new Option("請選擇對象", ""));
                    $.ajax({
                        url: "./get_account.php",
                        data: {
                            "ftype": $(this).val()
                        },
                        method: "POST",
                        dataType: "json"
                    }).done(function (data) {

                        for (i = 0; i < data['data'].length; i++) {
                            $("select[name='ftarget']").append(new Option(data['data'][i]["name"] + "(" + data['data'][i]["account"] + ")", data['data'][i]['account']));
                        }

                        $(".alert_global").hide();
                    });
                }
            });
            $("select[name='ftarget']").change(function () {
                if ($(this).val() != "") {
                    $(".alert_global").hide();
                }
            });

        });
        $(document).ready(function () {
            var table = $('#example').DataTable({
                "processing": true,
                "serverSide": true,
                "searching": false,
                "ajax": {
                    "url": "./invoice_data.php",
                    "type": "POST",
                    data: function (d) {
                        d.ftype = $("#ftype").val();
                        d.ftarget = $("#ftarget").val();
                        d.fsdate = $("#fsdate").val();
                        d.fedate = $("#fedate").val();
                        d.fstatus = $("#fstatus").val();
                        d.currency =  $("#currency").val();
                    },
                    dataSrc: function (d) {
                        $("#order_dir").val(d.order_dir);
                        $("#order_place").val(d.order_place);
                        return d.data;
                    }
                },
                responsive: true,
                fixedHeader: true,
                ordering: false,
                paging: false,
                dom: 'Blfrtip',
                columns: [
                    { "data": "opt" },
                    { "data": "order_num" },
                    { "data": "people" },
                    { "data": "type" },
                    { "data": "time" },
                    { "data": "status_content" },
                    { "data": "currency" },
                    { "data": "price" },
                    { "data": "invoice_people" },
                    { "data": "invoice_date" },
                ],
                buttons: [
                    {
                        extend: "print",
                        text: "列印",
                        className: "btn-primary",
                        title: '請款資料表',
                        exportOptions: {
                            columns: [1, 2, 3, 4, 5, 6, 7, 8],
                            customizeData: function (data) {
                                var options = {
                                    url: "./invoice_data.php",
                                    data: {
                                        ftype: $("#ftype").val(),
                                        ftarget: $("#ftarget").val(),
                                        fsdate: $("#fsdate").val(),
                                        fedate: $("#fedate").val(),
                                        fstatus: $("#fstatus").val(),
                                        currency: $("#currency").val(),
                                        start: '',
                                        length: '',
                                        "order[0][column]": $("#order_place").val(),
                                        "order[0][dir]": $("#order_dir").val(),
                                        "search[value]": $("#search_value").val(),
                                    },
                                    method: "POST",
                                    dataType: "json"
                                };
                                options.async = false;
                                options.success = function (res) {
                                    data.body = [];
                                    var columns = table.columns;
                                    var exps = [];
                                    console.log(table.columns);


                                    for (var i = 0; i < res.data.length; i++) {
                                        var obj = res.data[i];
                                        var newRow = [];
                                        newRow.push(obj["order_num"]);
                                        newRow.push(obj["people"]);
                                        newRow.push(obj["type"]);
                                        newRow.push(obj["time"]);
                                        newRow.push(obj["status_content"]);
                                        newRow.push(obj["currency"]);
                                        newRow.push(obj["price"]);
                                        newRow.push(obj["invoice_people"]);
                                        newRow.push(obj["invoice_date"]);
                                        data.body.push(newRow);
                                    }
                                };

                                $.ajax(options);
                            }
                        },
                    },
                    {
                        extend: "excel",
                        text: "儲存成Excel",
                        className: "btn-info",
                        title: '請款資料表',
                        exportOptions: {
                            columns: [1, 2, 3, 4, 5, 6, 7, 8]
                        },
                        customizeData: function (data) {
                            var options = {
                                url: "./invoice_data.php",
                                data: {
                                    ftype: $("#ftype").val(),
                                    ftarget: $("#ftarget").val(),
                                    fsdate: $("#fsdate").val(),
                                    fedate: $("#fedate").val(),
                                    fstatus: $("#fstatus").val(),
                                    currency: $("#currency").val(),
                                    start: '',
                                    length: '',
                                    "order[0][column]": $("#order_place").val(),
                                    "order[0][dir]": $("#order_dir").val(),
                                    "search[value]": $("#search_value").val(),
                                },
                                method: "POST",
                                dataType: "json"
                            };
                            options.async = false;
                            options.success = function (res) {
                                data.body = [];
                                var columns = table.columns;
                                for (var i = 0; i < res.data.length; i++) {
                                    var obj = res.data[i];
                                    var newRow = [];
                                    newRow.push(obj["order_num"]);
                                    newRow.push(obj["people"]);
                                    newRow.push(obj["type"]);
                                    newRow.push(obj["time"]);
                                    newRow.push(obj["status_content"]);
                                    newRow.push(obj["currency"]);
                                    newRow.push(obj["price"]);
                                    newRow.push(obj["invoice_people"]);
                                    newRow.push(obj["invoice_date"]);
                                    data.body.push(newRow);
                                }
                            };

                        }
                    },
                    {
                        text: '請款預覽',
                        action: function (e, dt, node, config) {
                            var ck = document.getElementsByName("someName[]");
                            var tlen = 0;
                            for (var i = 0; i < ck.length; i++) {
                                if (ck[i].checked) { tlen = tlen + 1; }
                            }
                            if (tlen > 0) {
                                $("input[name='options']").val("Y");
                                $(".edit_form").submit();
                            } else {
                                alert("請至少選擇一筆款項");
                            }

                        }
                    },
                    {
                        text: '廠商請款單預覽',
                        action: function (e, dt, node, config) {
                            $("input[name='options']").val("A");
                            $(".edit_form").submit();

                        }
                    }
                ],
                "language": {
                    // "lengthMenu": "每頁 _MENU_ 條紀錄",
                    "zeroRecords": "查無資料",
                    "info": "",
                    "infoEmpty": "共 _MAX_ 筆資料",
                    "infoFiltered": "(從 _MAX_ 條紀錄篩選)",
                    "paginate": {
                        "first": "第一頁",
                        "last": "最後一頁",
                        "next": "下一頁",
                        "previous": "上一頁",
                    },
                    // "search": "搜尋：",
                    "processing": "處理中"
                },

            });
            $("#search_btn").click(function () {
                let flag = true;
                if ($("select[name='ftype']").val() == '') {
                    flag = false;
                    $(".alert_global").html("請選擇身分");
                    $(".alert_global").show();
                } else if ($("select[name='ftarget'").val() == '') {
                    flag = false;
                    $(".alert_global").html("請選擇對象");
                    $(".alert_global").show();
                } else if ($("input[name='fsdate']").val() != '') {
                    if ($("input[name='fedate'").val() == '') {
                        flag = false;
                        $(".alert_global").html("請選擇結束日期");
                        $(".alert_global").show();
                    }
                } else if ($("input[name='fsdate']").val() != '') {
                    if ($("input[name='fedate'").val() == '') {
                        flag = false;
                        $(".alert_global").html("請選擇起始日期");
                        $(".alert_global").show();
                    }
                }

                if (flag) {
                    if ($("#loading_enable").val() == 'Y') {
                        if (new Date($("input[name='fsdate']").val()) > new Date($("input[name='fedate']").val())) {
                            $(".alert_global").html("結束日期不得小於起始日期");
                            $(".alert_global").show();
                        } else {
                            $("#loading_enable").val('N');

                            $("input[name='ser_type']").val($("select[name='ftype']").val());
                            $("input[name='ser_target']").val($("select[name='ftarget']").val());
                            $("input[name='ser_sdate']").val($("input[name='fsdate']").val());
                            $("input[name='ser_edate']").val($("input[name='fedate']").val());
                            $("input[name='ser_status']").val($("select[name='fstatus']").val());
                            table.clear();

                            table.ajax.reload(function(){
                                $("#loading_enable").val('Y');
                            });


                        }
                    } else {
                        $(".alert_global").html("資料讀取中...");
                        $(".alert_global").show();
                    }

                }
            });
        });
    </script>
</div>                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>Copyright © vteamsystem 2019-2020</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">確定要登出?</h5>
                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <div class="modal-body">確定要登出TBCCoin 後台管理系統</div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">取消</button>
                    <a class="btn btn-primary" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/logout.php">登出</a>
                </div>
            </div>
        </div>
    </div>


    <script src="./TBCCoin 後台管理系統_files/sb-admin-2.min.js.下載"></script>




<div id="ui-datepicker-div" class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" style="position: absolute; top: 127.3px; left: 1138.14px; z-index: 1; display: none;"><div class="ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-all"><a class="ui-datepicker-prev ui-corner-all" data-handler="prev" data-event="click" title="Prev"><span class="ui-icon ui-icon-circle-triangle-w">Prev</span></a><a class="ui-datepicker-next ui-corner-all" data-handler="next" data-event="click" title="Next"><span class="ui-icon ui-icon-circle-triangle-e">Next</span></a><div class="ui-datepicker-title"><select class="ui-datepicker-month" data-handler="selectMonth" data-event="change"><option value="0">Jan</option><option value="1" selected="selected">Feb</option><option value="2">Mar</option><option value="3">Apr</option><option value="4">May</option><option value="5">Jun</option><option value="6">Jul</option><option value="7">Aug</option><option value="8">Sep</option><option value="9">Oct</option><option value="10">Nov</option><option value="11">Dec</option></select><select class="ui-datepicker-year" data-handler="selectYear" data-event="change"><option value="2013">2013</option><option value="2014">2014</option><option value="2015">2015</option><option value="2016">2016</option><option value="2017">2017</option><option value="2018">2018</option><option value="2019">2019</option><option value="2020">2020</option><option value="2021">2021</option><option value="2022">2022</option><option value="2023" selected="selected">2023</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option><option value="2027">2027</option><option value="2028">2028</option><option value="2029">2029</option><option value="2030">2030</option><option value="2031">2031</option><option value="2032">2032</option><option value="2033">2033</option></select></div></div><table class="ui-datepicker-calendar"><thead><tr><th class="ui-datepicker-week-end"><span title="Sunday">Su</span></th><th><span title="Monday">Mo</span></th><th><span title="Tuesday">Tu</span></th><th><span title="Wednesday">We</span></th><th><span title="Thursday">Th</span></th><th><span title="Friday">Fr</span></th><th class="ui-datepicker-week-end"><span title="Saturday">Sa</span></th></tr></thead><tbody><tr><td class=" ui-datepicker-week-end ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">1</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">2</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">3</a></td><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">4</a></td></tr><tr><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">5</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">6</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">7</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">8</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">9</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">10</a></td><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">11</a></td></tr><tr><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">12</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">13</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">14</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">15</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">16</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">17</a></td><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">18</a></td></tr><tr><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">19</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">20</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">21</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">22</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">23</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">24</a></td><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">25</a></td></tr><tr><td class=" ui-datepicker-week-end " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">26</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">27</a></td><td class=" " data-handler="selectDay" data-event="click" data-month="1" data-year="2023"><a class="ui-state-default" href="https://www.tbcpharmacy.com/tbc_wallet/TBCBACKEND/invoice_management.php#">28</a></td><td class=" ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td><td class=" ui-datepicker-week-end ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled">&nbsp;</td></tr></tbody></table></div></body></html>
'''


soup = BeautifulSoup(html, 'html.parser')
#chrome.page_source
options = soup.find_all('option')