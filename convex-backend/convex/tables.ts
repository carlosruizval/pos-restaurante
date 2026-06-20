import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

// QUERY: obtener todas las mesas
export const getAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("tables").collect();
  },
});

// MUTATION: crear una mesa nueva
export const create = mutation({
  args: {
    number: v.number(),
    capacity: v.number(),
  },
  handler: async (ctx, args) => {
    const tableId = await ctx.db.insert("tables", {
      number: args.number,
      capacity: args.capacity,
      status: "free",
    });
    return tableId;
  },
});

// MUTATION: actualizar el estado de una mesa
export const updateStatus = mutation({
  args: {
    tableId: v.id("tables"),
    status: v.union(
      v.literal("free"),
      v.literal("occupied"),
      v.literal("waiting_payment")
    ),
  },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.tableId, { status: args.status });
  },
});