##Bug Oberservations##

1. PATCH /store/order/{order_id} endpoint returns 404 as a response
   even when I kept trying to update an order that already exists.

The usual expected behavior is something in the sense of PATCH being 
able to update the order status.

The current behavior is that the endpoint returns 404.

The usual impact would be like PATCH functionality seems like
it's not been implemented in the API.

This concludes my observations on the report.

