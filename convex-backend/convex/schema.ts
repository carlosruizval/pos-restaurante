import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
    password_hash: v.string(),
    role: v.union(
      v.literal("admin"),
      v.literal("cajero"),
      v.literal("mesero"),
      v.literal("cocina")
    ),
    active: v.boolean(),
  }),

  tables: defineTable({
    number: v.number(),
    capacity: v.number(),
    status: v.union(
      v.literal("free"),
      v.literal("occupied"),
      v.literal("waiting_payment")
    ),
    assigned_waiter: v.optional(v.id("users")),
    current_order: v.optional(v.id("orders")),
  }),

  categories: defineTable({
    name: v.string(),
    sort_order: v.number(),
  }),

  products: defineTable({
    name: v.string(),
    price: v.number(),
    category_id: v.id("categories"),
    available: v.boolean(),
    description: v.string(),
  }),

  orders: defineTable({
    table_id: v.id("tables"),
    waiter_id: v.id("users"),
    status: v.union(
      v.literal("pending"),
      v.literal("preparing"),
      v.literal("ready"),
      v.literal("delivered"),
      v.literal("paid")
    ),
    items: v.array(
      v.object({
        product_id: v.id("products"),
        product_name: v.string(),
        quantity: v.number(),
        unit_price: v.number(),
      })
    ),
    total: v.number(),
    created_at: v.number(),
    paid_at: v.optional(v.number()),
  }),

  payments: defineTable({
    order_id: v.id("orders"),
    method: v.union(
      v.literal("cash"),
      v.literal("card"),
      v.literal("transfer")
    ),
    amount: v.number(),
    discount: v.number(),
    tip: v.number(),
    cashier_id: v.id("users"),
    created_at: v.number(),
  }),

  ingredients: defineTable({
    name: v.string(),
    unit: v.string(),
    stock: v.number(),
    min_stock: v.number(),
  }),

  product_ingredients: defineTable({
    product_id: v.id("products"),
    ingredient_id: v.id("ingredients"),
    quantity_used: v.number(),
  }),
});