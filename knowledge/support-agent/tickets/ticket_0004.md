# Ticket 0004: User "heba" Cannot Access Customers in CustomerPromotionGroupLink

* **Date & Time**: 2026-06-23
* **System Component**: Back Office (Permissions)
* **Symptom Category**: Access Control / Permissions
* **Reported Issue**:
  User "heba" cannot see customers in the CustomerPromotionGroupLink screen in the BO, while the admin can see all customers. The list appears empty or restricted for "heba".

---

## Root Cause & Diagnosis

The BO uses a role/permission-based access control system. Each user's permissions determine which records and screens they can view. User "heba" did not have sufficient permissions to view customers in the CustomerPromotionGroupLink context.

The Permissions tab in the BO contains granular toggles for various features and data access levels. When a user lacks the required permissions, certain records (like customers linked to promotion groups) are hidden from their view, even though the data exists in the database and is visible to admin users.

---

## Solution

1. Log in to the BO as an admin
2. Go to **Settings → Users → Permissions** (or the Permissions tab for the relevant user/role)
3. Select user **"heba"**
4. Check the **"Allow All Permissions"** box (or explicitly enable the missing permission related to CustomerPromotionGroupLink / customer data access)
5. Save the changes
6. Ask "heba" to log out and log back in — the customers should now be visible in CustomerPromotionGroupLink

---

## Verification Result

After enabling "Allow All Permissions" for user "heba" in the Permissions tab, the user can now access and view all customers in the CustomerPromotionGroupLink screen, matching the admin's view.
