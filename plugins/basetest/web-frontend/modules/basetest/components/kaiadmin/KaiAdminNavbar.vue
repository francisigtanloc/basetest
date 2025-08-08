<template>
  <div class="main-header">
    <div class="main-header-logo">
      <!-- Logo Header -->
      <div class="logo-header" data-background-color="dark">
        <nuxt-link to="/kaiadmin/dashboard" class="logo">
          <img
            src="@basetest/assets/img/kaiadmin/logo_light.svg"
            alt="navbar brand"
            class="navbar-brand"
            height="20"
          />
        </nuxt-link>
        <div class="nav-toggle">
          <button class="btn btn-toggle toggle-sidebar">
            <i class="gg-menu-right"></i>
          </button>
          <button class="btn btn-toggle sidenav-toggler">
            <i class="gg-menu-left"></i>
          </button>
        </div>
        <button class="topbar-toggler more">
          <i class="gg-more-vertical-alt"></i>
        </button>
      </div>
      <!-- End Logo Header -->
    </div>
    <!-- Navbar Header -->
    <nav class="navbar navbar-header navbar-header-transparent navbar-expand-lg border-bottom">
      <div class="container-fluid">
        <nav class="navbar navbar-header-left navbar-expand-lg navbar-form nav-search p-0 d-none d-lg-flex">
          <div class="input-group">
            <div class="input-group-prepend">
              <button type="submit" class="btn btn-search pe-1">
                <i class="fa fa-search search-icon"></i>
              </button>
            </div>
            <input
              type="text"
              placeholder="Search ..."
              class="form-control"
              v-model="searchQuery"
              @keyup.enter="performSearch"
            />
          </div>
        </nav>

        <ul class="navbar-nav topbar-nav ms-md-auto align-items-center">
          <li class="nav-item topbar-icon dropdown hidden-caret d-flex d-lg-none">
            <a
              class="nav-link dropdown-toggle"
              data-bs-toggle="dropdown"
              href="#"
              role="button"
              aria-expanded="false"
              aria-haspopup="true"
            >
              <i class="fa fa-search"></i>
            </a>
            <ul class="dropdown-menu dropdown-search animated fadeIn">
              <form class="navbar-left navbar-form nav-search">
                <div class="input-group">
                  <input
                    type="text"
                    placeholder="Search ..."
                    class="form-control"
                    v-model="mobileSearchQuery"
                    @keyup.enter="performMobileSearch"
                  />
                </div>
              </form>
            </ul>
          </li>
          <li class="nav-item topbar-icon dropdown hidden-caret">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="messageDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i class="fa fa-envelope"></i>
            </a>
            <ul class="dropdown-menu messages-notif-box animated fadeIn" aria-labelledby="messageDropdown">
              <li>
                <div class="dropdown-title d-flex justify-content-between align-items-center">
                  Messages
                  <a href="#" class="small" @click="markAllMessagesRead">Mark all as read</a>
                </div>
              </li>
              <li>
                <div class="message-notif-scroll scrollbar-outer">
                  <div class="notif-center">
                    <a href="#" v-for="message in messages" :key="message.id" @click="openMessage(message)">
                      <div class="notif-img">
                        <img
                          :src="`@basetest/assets/img/${message.avatar}`"
                          alt="Img Profile"
                        />
                      </div>
                      <div class="notif-content">
                        <span class="subject">{{ message.from }}</span>
                        <span class="block">{{ message.text }}</span>
                        <span class="time">{{ message.time }}</span>
                      </div>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <a class="see-all" href="#" @click="seeAllMessages">
                  See all messages<i class="fa fa-angle-right"></i>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item topbar-icon dropdown hidden-caret">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="notifDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i class="fa fa-bell"></i>
              <span class="notification" v-if="notifications.length > 0">{{ notifications.length }}</span>
            </a>
            <ul class="dropdown-menu notif-box animated fadeIn" aria-labelledby="notifDropdown">
              <li>
                <div class="dropdown-title">
                  You have {{ notifications.length }} new notification{{ notifications.length !== 1 ? 's' : '' }}
                </div>
              </li>
              <li>
                <div class="notif-scroll scrollbar-outer">
                  <div class="notif-center">
                    <a href="#" v-for="notif in notifications" :key="notif.id" @click="openNotification(notif)">
                      <div class="notif-icon" :class="notif.iconClass" v-if="notif.icon">
                        <i :class="notif.icon"></i>
                      </div>
                      <div class="notif-img" v-else-if="notif.avatar">
                        <img
                          :src="`@basetest/assets/img/${notif.avatar}`"
                          alt="Img Profile"
                        />
                      </div>
                      <div class="notif-content">
                        <span class="block">{{ notif.text }}</span>
                        <span class="time">{{ notif.time }}</span>
                      </div>
                    </a>
                  </div>
                </div>
              </li>
              <li>
                <a class="see-all" href="#" @click="seeAllNotifications">
                  See all notifications<i class="fa fa-angle-right"></i>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item topbar-icon dropdown hidden-caret">
            <a
              class="nav-link"
              data-bs-toggle="dropdown"
              href="#"
              aria-expanded="false"
            >
              <i class="fas fa-layer-group"></i>
            </a>
            <div class="dropdown-menu quick-actions animated fadeIn">
              <div class="quick-actions-header">
                <span class="title mb-1">Quick Actions</span>
                <span class="subtitle op-7">Shortcuts</span>
              </div>
              <div class="quick-actions-scroll scrollbar-outer">
                <div class="quick-actions-items">
                  <div class="row m-0">
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('calendar')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-danger rounded-circle">
                          <i class="far fa-calendar-alt"></i>
                        </div>
                        <span class="text">Calendar</span>
                      </div>
                    </a>
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('maps')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-warning rounded-circle">
                          <i class="fas fa-map"></i>
                        </div>
                        <span class="text">Maps</span>
                      </div>
                    </a>
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('reports')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-info rounded-circle">
                          <i class="fas fa-file-excel"></i>
                        </div>
                        <span class="text">Reports</span>
                      </div>
                    </a>
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('emails')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-success rounded-circle">
                          <i class="fas fa-envelope"></i>
                        </div>
                        <span class="text">Emails</span>
                      </div>
                    </a>
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('invoice')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-primary rounded-circle">
                          <i class="fas fa-file-invoice-dollar"></i>
                        </div>
                        <span class="text">Invoice</span>
                      </div>
                    </a>
                    <a class="col-6 col-md-4 p-0" href="#" @click="quickAction('payments')">
                      <div class="quick-actions-item">
                        <div class="avatar-item bg-secondary rounded-circle">
                          <i class="fas fa-credit-card"></i>
                        </div>
                        <span class="text">Payments</span>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </li>

          <li class="nav-item topbar-user dropdown hidden-caret">
            <a
              class="dropdown-toggle profile-pic"
              data-bs-toggle="dropdown"
              href="#"
              aria-expanded="false"
            >
              <div class="avatar-sm">
                <img
                  src="@basetest/assets/img/profile.jpg"
                  alt="..."
                  class="avatar-img rounded-circle"
                />
              </div>
              <span class="profile-username">
                <span class="op-7">Hi,</span>
                <span class="fw-bold">{{ currentUser.name }}</span>
              </span>
            </a>
            <ul class="dropdown-menu dropdown-user animated fadeIn">
              <div class="dropdown-user-scroll scrollbar-outer">
                <li>
                  <div class="user-box">
                    <div class="avatar-lg">
                      <img
                        src="@basetest/assets/img/profile.jpg"
                        alt="image profile"
                        class="avatar-img rounded"
                      />
                    </div>
                    <div class="u-text">
                      <h4>{{ currentUser.name }}</h4>
                      <p class="text-muted">{{ currentUser.email }}</p>
                      <nuxt-link
                        to="/kaiadmin/profile"
                        class="btn btn-xs btn-secondary btn-sm"
                      >
                        View Profile
                      </nuxt-link>
                    </div>
                  </div>
                </li>
                <li>
                  <div class="dropdown-divider"></div>
                  <nuxt-link class="dropdown-item" to="/kaiadmin/profile">My Profile</nuxt-link>
                  <a class="dropdown-item" href="#" @click="showBalance">My Balance</a>
                  <a class="dropdown-item" href="#" @click="showInbox">Inbox</a>
                  <div class="dropdown-divider"></div>
                  <nuxt-link class="dropdown-item" to="/kaiadmin/settings">Account Setting</nuxt-link>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="#" @click="logout">Logout</a>
                </li>
              </div>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    <!-- End Navbar -->
  </div>
</template>

<script>
export default {
  name: 'KaiAdminNavbar',
  data() {
    return {
      searchQuery: '',
      mobileSearchQuery: '',
      currentUser: {
        name: 'Hizrian',
        email: 'hello@example.com'
      },
      messages: [
        {
          id: 1,
          from: 'Jimmy Denis',
          text: 'How are you ?',
          time: '5 minutes ago',
          avatar: 'jm_denis.jpg'
        },
        {
          id: 2,
          from: 'Chad',
          text: 'Ok, Thanks !',
          time: '12 minutes ago',
          avatar: 'chadengle.jpg'
        },
        {
          id: 3,
          from: 'Jhon Doe',
          text: 'Ready for the meeting today...',
          time: '12 minutes ago',
          avatar: 'mlane.jpg'
        },
        {
          id: 4,
          from: 'Talha',
          text: 'Hi, Apa Kabar ?',
          time: '17 minutes ago',
          avatar: 'talha.jpg'
        }
      ],
      notifications: [
        {
          id: 1,
          text: 'New user registered',
          time: '5 minutes ago',
          icon: 'fa fa-user-plus',
          iconClass: 'notif-primary'
        },
        {
          id: 2,
          text: 'Rahmad commented on Admin',
          time: '12 minutes ago',
          icon: 'fa fa-comment',
          iconClass: 'notif-success'
        },
        {
          id: 3,
          text: 'Reza send messages to you',
          time: '12 minutes ago',
          avatar: 'profile2.jpg'
        },
        {
          id: 4,
          text: 'Farrah liked Admin',
          time: '17 minutes ago',
          icon: 'fa fa-heart',
          iconClass: 'notif-danger'
        }
      ]
    }
  },
  methods: {
    performSearch() {
      if (this.searchQuery.trim()) {
        this.$swal({
          title: 'Search',
          text: `Searching for: "${this.searchQuery}"`,
          type: 'info',
          confirmButtonText: 'OK'
        })
      }
    },
    performMobileSearch() {
      if (this.mobileSearchQuery.trim()) {
        this.$swal({
          title: 'Search',
          text: `Searching for: "${this.mobileSearchQuery}"`,
          type: 'info',
          confirmButtonText: 'OK'
        })
      }
    },
    markAllMessagesRead() {
      this.$swal({
        title: 'Success!',
        text: 'All messages marked as read',
        type: 'success',
        confirmButtonText: 'OK'
      })
    },
    openMessage(message) {
      this.$swal({
        title: `Message from ${message.from}`,
        text: message.text,
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    seeAllMessages() {
      this.$router.push('/kaiadmin/messages')
    },
    openNotification(notification) {
      this.$swal({
        title: 'Notification',
        text: notification.text,
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    seeAllNotifications() {
      this.$router.push('/kaiadmin/notifications')
    },
    quickAction(action) {
      this.$swal({
        title: 'Quick Action',
        text: `Opening ${action}...`,
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    showBalance() {
      this.$swal({
        title: 'My Balance',
        text: 'Current balance: $1,234.56',
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    showInbox() {
      this.$router.push('/kaiadmin/inbox')
    },
    logout() {
      this.$swal({
        title: 'Are you sure?',
        text: 'You will be logged out!',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, logout!'
      }).then((result) => {
        if (result.value) {
          this.$swal(
            'Logged out!',
            'You have been logged out successfully.',
            'success'
          ).then(() => {
            this.$router.push('/login')
          })
        }
      })
    }
  }
}
</script>