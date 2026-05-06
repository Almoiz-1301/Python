print("Hello, Almoiz How are You !")
'''
/**
 * Sets the subscription tier for the user based on either organization or org admin Stripe id.
 * @param user - The user to update
 * @param stripeCustomerID - Optional Org admin Stripe customer ID, if known
 */
export async function setTierFromStripe(user: MCUser, stripeCustomerID?: string) {
  let customerID = stripeCustomerID;
  if (!customerID) {
    const customer = await getStripeCustomerByUser(user);
    customerID = customer?.customerId;
  }
  const update = await determineSubscriptionUpdate(customerID);
  await updateUser(user.id, update, undefined, user.subscriptionTier);
}
'''
# This is a comment and will not be executed which is in the triple quotes called as multi-line comment
#Below is an example of single line comment
# print("This line is commented and will not be executed")
